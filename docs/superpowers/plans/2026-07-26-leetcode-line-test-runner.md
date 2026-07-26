# LeetCode Line Test Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Read each non-empty text-file line as positional arguments for a `Solution` method and print every execution result.

**Architecture:** `test_runner.py` owns safe line parsing and iteration. Each problem file passes its bound `Solution` method or a problem-specific wrapper to `run_cases`, so parameter order follows that method's definition without hard-coding problem semantics in the runner.

**Tech Stack:** Python standard library (`ast`, `pathlib`, `unittest`, `io`, `tempfile`)

---

### Task 1: Parse one line into method arguments

**Files:**
- Create: `python/leetcode/test_test_runner.py`
- Create: `python/leetcode/test_runner.py`

- [ ] **Step 1: Write failing parser tests**

```python
import unittest

from test_runner import parse_case


class ParseCaseTest(unittest.TestCase):
    def test_parses_values_as_positional_arguments(self):
        self.assertEqual(parse_case("[3,2,2,3], 3"), ([3, 2, 2, 3], 3))

    def test_wraps_one_parameter_as_one_argument(self):
        self.assertEqual(parse_case("[1,2,3]"), ([1, 2, 3],))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run parser tests and verify RED**

Run: `python3 -m unittest python/leetcode/test_test_runner.py -v`

Expected: ERROR because `test_runner` does not exist.

- [ ] **Step 3: Implement safe parser**

```python
from ast import literal_eval


def parse_case(line: str) -> tuple:
    parsed = literal_eval(f"({line.strip()})")
    return parsed if isinstance(parsed, tuple) else (parsed,)
```

- [ ] **Step 4: Run parser tests and verify GREEN**

Run: `python3 -m unittest python/leetcode/test_test_runner.py -v`

Expected: 2 tests pass.

### Task 2: Iterate cases and continue after failures

**Files:**
- Modify: `python/leetcode/test_test_runner.py`
- Modify: `python/leetcode/test_runner.py`

- [ ] **Step 1: Write failing iteration test**

Add imports and this test class:

```python
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from test_runner import parse_case, run_cases


class RunCasesTest(unittest.TestCase):
    def test_runs_non_empty_lines_and_continues_after_an_error(self):
        with TemporaryDirectory() as directory:
            case_file = Path(directory) / "cases.txt"
            case_file.write_text("1, 2\n\ninvalid(\n3, 4\n", encoding="utf-8")
            calls = []
            output = StringIO()

            def add(left, right):
                calls.append((left, right))
                return left + right

            with redirect_stdout(output):
                run_cases(case_file, add)

        self.assertEqual(calls, [(1, 2), (3, 4)])
        self.assertIn("Case 1", output.getvalue())
        self.assertIn("result: 3", output.getvalue())
        self.assertIn("Case 2 error:", output.getvalue())
        self.assertIn("Case 3", output.getvalue())
        self.assertIn("result: 7", output.getvalue())
```

- [ ] **Step 2: Run iteration test and verify RED**

Run: `python3 -m unittest python/leetcode/test_test_runner.py -v`

Expected: ERROR because `run_cases` is not defined.

- [ ] **Step 3: Implement iteration and output**

```python
from ast import literal_eval
from collections.abc import Callable
from pathlib import Path
from typing import Any


def parse_case(line: str) -> tuple:
    parsed = literal_eval(f"({line.strip()})")
    return parsed if isinstance(parsed, tuple) else (parsed,)


def run_cases(case_file: str | Path, run_case: Callable[..., Any]) -> None:
    lines = Path(case_file).read_text(encoding="utf-8").splitlines()
    case_number = 0

    for line in lines:
        if not line.strip():
            continue

        case_number += 1
        try:
            arguments = parse_case(line)
            result = run_case(*arguments)
            print(f"Case {case_number}")
            print(f"  input: {arguments}")
            print(f"  result: {result}")
        except Exception as error:
            print(f"Case {case_number} error: {error}")
```

- [ ] **Step 4: Run all runner tests and verify GREEN**

Run: `python3 -m unittest python/leetcode/test_test_runner.py -v`

Expected: 3 tests pass.

### Task 3: Connect the current LeetCode problem

**Files:**
- Create: `python/leetcode/leet_test.txt`
- Modify: `python/leetcode/leet_test.py`

- [ ] **Step 1: Add sample cases**

```text
[3,2,2,3], 3
[1,2,3,3,4], 3
```

- [ ] **Step 2: Add the executable entry point**

Append:

```python
from pathlib import Path

from test_runner import run_cases


if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().removeElement)
```

- [ ] **Step 3: Execute the problem file**

Run: `python3 python/leetcode/leet_test.py`

Expected: two numbered cases are printed in input order. The current unfinished solution's return value is printed as `None`; the runner does not change solution behavior.

- [ ] **Step 4: Run the regression tests**

Run: `python3 -m unittest python/leetcode/test_test_runner.py -v`

Expected: all 3 tests pass without errors.

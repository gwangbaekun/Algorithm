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
            input_display = repr(arguments)
            result = run_case(*arguments)
            print(f"Case {case_number}")
            print(f"  input: {input_display}")
            print(f"  result: {result}")
        except Exception as error:
            print(f"Case {case_number} error: {type(error).__name__}: {error}")

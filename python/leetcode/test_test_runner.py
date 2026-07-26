from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from leet_test import Solution, run_remove_element
from test_runner import parse_case, run_cases


class ParseCaseTest(unittest.TestCase):
    def test_parses_values_as_positional_arguments(self):
        self.assertEqual(parse_case("[3,2,2,3], 3"), ([3, 2, 2, 3], 3))

    def test_wraps_one_parameter_as_one_argument(self):
        self.assertEqual(parse_case("[1,2,3]"), ([1, 2, 3],))


class SolutionTest(unittest.TestCase):
    def test_returns_remaining_count_and_places_values_in_prefix(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]

        k = Solution().removeElement(nums, 2)

        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_terminal_result_contains_only_checked_prefix(self):
        result = run_remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)

        self.assertEqual(result, (5, [0, 1, 3, 0, 4]))


class RunCasesTest(unittest.TestCase):
    def test_prints_input_before_solution_mutates_it(self):
        with TemporaryDirectory() as directory:
            case_file = Path(directory) / "cases.txt"
            case_file.write_text("[1,2], 2\n", encoding="utf-8")
            output = StringIO()

            def mutate(values, _):
                values.pop()

            with redirect_stdout(output):
                run_cases(case_file, mutate)

        self.assertIn("input: ([1, 2], 2)", output.getvalue())

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


if __name__ == "__main__":
    unittest.main()

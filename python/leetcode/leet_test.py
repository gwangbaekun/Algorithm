from itertools import count
from pathlib import Path
from typing import List

from test_runner import run_cases


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 10e9 + 1
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1

        return candidate


if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().majorityElement)

from itertools import count
from pathlib import Path
from typing import List

from test_runner import run_cases


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().majorityElement)

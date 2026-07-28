from itertools import count
from pathlib import Path
from typing import List

from test_runner import run_cases


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
                count = 0
            elif nums[i-1] == nums[i] and count == 0:
                nums[idx] = nums[i]
                idx += 1
                count += 1
            elif nums[i-1] == nums[i] and count >= 1:
                count += 1
        return idx, nums



if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().removeDuplicates)

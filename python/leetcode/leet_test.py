from pathlib import Path
from typing import List

from test_runner import run_cases


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for el in nums:
            if el != val:
                nums[k] = el
                k += 1

        return k



if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().removeElement)

from itertools import count
from pathlib import Path
from typing import List

from test_runner import run_cases


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                sum += prices[i] - prices[i - 1]
        return sum


if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().maxProfit)

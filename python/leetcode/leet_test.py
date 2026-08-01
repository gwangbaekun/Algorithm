from itertools import count
from pathlib import Path
from typing import List

from test_runner import run_cases


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for p in prices:
            min_price = min(min_price, p)
            best = max(best, p - min_price)
        return best


if __name__ == "__main__":
    case_file = Path(__file__).with_suffix(".txt")
    run_cases(case_file, Solution().maxProfit)

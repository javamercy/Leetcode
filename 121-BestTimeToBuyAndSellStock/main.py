import sys


class Solution:
    def maxProfit1(self, prices: list[int]) -> int:
        l: int = 0
        r: int = 1
        profit: int = 0

        while r < len(prices):
            curr = prices[r] - prices[l]

            if curr > profit:
                profit = curr
            elif curr < 0:
                l = r

            r += 1

        return profit

    def maxProfit2(self, prices: list[int]) -> int:
        min_price: int = sys.maxsize
        dp: list[int] = [0] * (len(prices) + 1)

        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price

            curr = price - min_price
            if curr > dp[i]:
                dp[i + 1] = curr
            else:
                dp[i + 1] = dp[i]

        return dp[-1]

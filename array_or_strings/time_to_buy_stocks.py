class Solution:
    def maxProfit2Pointer(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l] )

            else:
                l = r
            r += 1



    def maxProfit(self, prices):
        buy_price = 0
        profit = 0

        for p in profit[1:]:
            if buy_price > p:
                buy_price = p

            profit = max(profit, p - buy_price)
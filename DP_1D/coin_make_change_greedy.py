class Solution:

    def make_change(self, amount, coins):
        coins.sort(reverse = True)
        res = []
        remaining = amount

        for coin in coins:
            while remaining >= coin:
                res.append(coin)
                remaining -= coin

        return res

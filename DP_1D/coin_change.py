from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        size = amount + 1
        dp = [float('inf')] * size
        dp[0] = 0

        for target in range(1, size):
            for coin in coins:
                if (target - coin) >= 0:
                    dp[target] = min(dp[target], dp[target-coin] + 1)
        # O(n * coin) time, O(n) space
        return dp[amount] if dp[amount] != float('inf') else -1




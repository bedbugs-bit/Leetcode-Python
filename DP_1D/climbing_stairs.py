from typing import List


class Solution:
    def climbing_stairs_recursion(self,n:int):
        if n == 0 or n == 1:
            return 1
        return self.climbing_stairs(n-1) + self.climbing_stairs(n-2)

    def climbing_stairs_dp(self, n):
        dp = [0] * n + 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]




        


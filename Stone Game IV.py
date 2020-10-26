#Stone Game IV

class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5 + 1)):
                if not dp[i - j * j]:
                    dp[i] = 1
                    break
        return dp[n]
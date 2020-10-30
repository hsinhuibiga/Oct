#Number of Longest Increasing Subsequence

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLIS= ans = 0
        size = len(nums)
        dp = [1] * size
        dz = [1] * size
        for x in range(size):
            for y in range(0, x):
                if nums[x] > nums[y]:
                    if dp[y] + 1 > dp[x]:
                        dp[x] = dp[y] + 1
                        dz[x] = dz[y]
                    elif dp[y] + 1 == dp[x]:
                        dz[x] += dz[y]
        maxLIS = max(dp + [0])
        ans = 0
        for p, z in zip(dp, dz):
            if p == maxLIS:
                ans += z
        return ans
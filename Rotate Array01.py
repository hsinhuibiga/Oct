#Rotate Array

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        changed = nums[-k:] + nums[:-k]
        for i in range(len(changed)):
            nums[i] = changed[i]
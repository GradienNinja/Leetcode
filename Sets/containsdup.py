# problem link https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self,nums):
        n = len(nums)
        unique_values = set()
        for i in range(n):
            if nums[i] in unique_values:
                return True 
            unique_values.add(nums[i])

        return False

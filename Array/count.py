# problem link https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
  def removeDuplicates(self,nums):
    n = len(nums) 
    if n == 0:
      return 0 
    k = 1 
    for i in range(1,n):
      if nums[i] != nums[i - 1]:
        nums[k] = nums[i] 
        k = k + 1 
    return nums[:k]
    
    
nums = [1,1,2,3,4]
result = Solution()
print(result.removeDuplicates(nums))

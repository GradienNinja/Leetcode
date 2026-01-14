#problem link https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array

class Solution:
  def searchInsert(self,nums,target):
    left = 0 
    right = len(nums) - 1 
    while left <= right:
      mid = (left + right) // 2 
      if nums[mid] == target:
        return mid 
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
        
    return left
    
    
result = Solution()
nums = [1,3,5,6]
target = 2
print(result.searchInsert(nums,target))

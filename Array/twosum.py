# https://leetcode.com/problems/two-sum/

class Solution:
  def __init__(self,nums,target):
    for i in range(len(nums)):
      for j in range(i+1,len(num)):
        if nums[i] + nums[j] == target:
          return [i,j] 
          
    return [] 
    
    

# problem link https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums, target):
        # 1️⃣ Find the first occurrence
        left = 0
        right = len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # Target must be on the right side
                left = mid + 1
            elif nums[mid] > target:
                # Target must be on the left side
                right = mid - 1
            else:
                # Found target, save it as first and move left to check earlier occurrences
                first = mid
                right = mid - 1

        # 2️⃣ Find the last occurrence
        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # Target must be on the right side
                left = mid + 1
            elif nums[mid] > target:
                # Target must be on the left side
                right = mid - 1
            else:
                # Found target, save it as last and move right to check later occurrences
                last = mid
                left = mid + 1

        # 3️⃣ Return the first and last indices
        return [first, last]


# Test
nums = [5,7,7,8,8,10]
target = 8

result = Solution()
print(result.searchRange(nums, target))

# Given an array of integers nums and an integer target,
# return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:
# Input:
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10

# Output: [0,2]

# Solution: Build hashmap and check membership
# Time: O(n) as we iterate over list to build hash
# Space: O(n) as hash grows to size n worst case

# create an empty hashmap
# iterate over nums with index i
#   calculate difference = target - nums[i]
#   if difference is in hashmap:
#       return [hashmap[difference], i]
#   else store nums[i] and its index i in hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in check:
                return [check[difference], i]
            check[num] = i


sol = Solution()
print(sol.twoSum([3,4,5,6], 7))
print(sol.twoSum([4,5,6], 10))

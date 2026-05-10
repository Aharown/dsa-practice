from typing import List
from collections import Counter

# Given an integer array nums, return true if any value appears
# more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]

# Output: true

# build freq hash map (keys array vals, values freq of numbers)
# iterate over values values = freq.values()
# for val in values
# if n > 1
# return true immediately


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        values = freq.values()
        for val in values:
            if val > 1:
                return True
        return False



s = Solution()
print(s.hasDuplicate([1, 2, 3, 3]))
print(s.hasDuplicate([1, 2, 3, 4]))

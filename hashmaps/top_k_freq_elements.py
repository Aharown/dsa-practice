from typing import List
from collections import Counter

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

#pseudocode
# assign count var counter(nums) returns dict with counts as vals
# get keys transform into list and pass into sorted(count.keys, reverse=True)
# assign slice from start 0-k to result var
# return result

# Time: O(n log n) sorting the keys is O(n log n)
# Space: O(n) building a new dictionary and list are both O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        result = sorted_keys[0:k]

        return result

sol = Solution()

print(sol.topKFrequent([7,7,8], 1))
print(sol.topKFrequent([1,2,2,3,3,3], 2))
print(sol.topKFrequent([7,7,8,8,9,9], 3))

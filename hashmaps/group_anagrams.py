from collections import defaultdict
from typing import List

# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]

#pseudocode
# dictionary initialised with empty list (keys are input sorted strings, values are lists of strings that are anagrams of keys)
# iterate over input list with for loop and push strings into lists if the strings match the keys.sorted
# return dictionary values back as a 2d list list(dict)

# Time: O(n * k log k) sorting each of n strings of length k
# Space: O(n) storing every string in the hashmap once

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())


sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(sol.groupAnagrams(["x"]))

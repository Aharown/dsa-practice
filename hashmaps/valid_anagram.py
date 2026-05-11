from collections import Counter

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

# Solution 1: Sort (brute force)
# Time: O(n log n) as both strings are sorted
# Space: O(n) as sorted() creates a new list for each string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted

# Solution 2: Counter
# Time: O(n) to build each counter hashmap
# Space: O(n) as counter() creates freq hashmap for each string
# pass strs into counter functions
# test for equality

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter = Counter(s)
        tcounter = Counter(t)
        return scounter == tcounter

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))

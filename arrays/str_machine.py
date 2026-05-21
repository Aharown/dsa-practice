from typing import List

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network
# and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }

# Machine 2 (receiver) has the function:

# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }

# So Machine 1 does:

# String encoded_string = encode(strs);

# and Machine 2 does:

# List<String> decoded_strs = decode(encoded_string);

# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:

# Input: strs = ["Hello","World"]

# Output: ["Hello","World"]

# Explanation:

# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

# // Machine 1 ---encoded_string---> Machine 2
# List<String> decoded_strs = solution.decode(encoded_string);

#pseudocode
# encode
# empty string to append strings to
# loop over input list
# append words with prefixed length and delimeter
# return strinf
# decode
# empty list to push words
# 2 pointer solution - init pointer to 0
# outer while loop i <- length of str
# init second pointer as i
# inner while loop pointer j is not on delimeter
# move j forward until delim is reached
# get length of word pointers are currently on
# slice the word and append to list
# return result

# encode — Time: O(n) iterating over list, Space: O(n) building encoded string
# decode — Time: O(n) single pass through encoded string, Space: O(n) building result list

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result


sol = Solution()
print(sol.encode(['Hello', 'World']))
print(sol.decode("5#Hello5#World"))

print(sol.encode(['neat']))
print(sol.decode("4#neat"))

print(sol.encode(['co#de']))
print(sol.decode("5#co#de"))

# dsa-practice

Structured DSA practice working through the [NeetCode 150](https://neetcode.io), organised by topic. Each solution is written in Python, tested manually, and committed with a note on the approach and complexity.

This repo is part of a structured self-directed engineering study programme alongside CS50P coursework and independent project work.

---

## Structure

```
dsa-practice/
├── arrays/
│   ├── contains_duplicate.py
│   └── two_sum.py
├── hashmaps/
│   └── valid_anagram.py
├── two_pointers/
├── sliding_window/
├── stack/
├── binary_search/
├── linked_lists/
├── trees/
├── heap/
├── backtracking/
├── graphs/
└── dynamic_programming/
```

---

## Approach

Each solution file includes a comment at the top covering:

- The pattern or technique used
- Time and space complexity
- Any alternative approaches considered
Example:

```python
# Approach: set for O(1) lookups
# Time: O(n) — iterate once through nums
# Space: O(n) — set grows up to n elements

class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
```

Problems are solved locally in VS Code, manually tested by instantiating the `Solution` class, then committed and pushed.

---

## Stack

- Python 3
- VS Code
- Git / GitHub
---

## Progress

| Topic | Status |
|---|---|
| Arrays & Hashing | In progress |
| Two Pointers | Not started |
| Sliding Window | Not started |
| Stack | Not started |
| Binary Search | Not started |
| Linked Lists | Not started |
| Trees | Not started |
| Heap / Priority Queue | Not started |
| Backtracking | Not started |
| Graphs | Not started |
| Dynamic Programming | Not started |

---

## Status

In progress. Updated consistently as new problems are completed.

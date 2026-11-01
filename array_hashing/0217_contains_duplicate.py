"""
Problem:     0217. Contains Duplicate
Difficulty:  Easy
Link:        https://leetcode.com/problems/contains-duplicate/
Topic:       Arrays & Hashing

Approach:
    1. Brute Force: Compare every pair using nested loops -> O(n^2) Time, O(1) Space.
    2. Sorting: Sort the array and check adjacent elements -> O(n log n) Time, O(1) Space.
    3. Optimal (Hash Set): Iterate through the array while storing seen numbers in a set.
       If the current number is already in the set, a duplicate exists -> return True.
       If traversal finishes with no duplicates found -> return False.

Complexity:
    - Time:  O(n) - Single linear pass; set lookups and insertions are O(1) on average.
    - Space: O(n) - In the worst case (all unique elements), the set stores n items.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Local Test Harness
if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) is True, "Test 1 Failed"
    assert sol.containsDuplicate([1, 2, 3, 4]) is False, "Test 2 Failed"
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True, "Test 3 Failed"
    print("✓ All test cases passed!")
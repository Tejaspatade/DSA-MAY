"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
"""
class Solution:
    def containsDuplicate(self, nums) -> bool:
        # Use a HashMap, Store every new element found,
        # if found a duplicate, exit out of loop and return false
        # SC: O(n)
        hashMap = {}
        # Iterate Thru All Nums
        for num in nums:
            # Finding num in HashMap O(1) time
            if num in hashMap:
                # Found a duplicate, terminate loop
                return True
            else:
                hashMap[num] = 1
        # If execution reaches here, array had all distinct values
        return False
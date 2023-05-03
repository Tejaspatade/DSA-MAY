"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""
class Solution:
    def trap(self, height) -> int:
        if not height: return 0
        # Left & right pointers
        l, r = 0, len(height) - 1

        # Max yet from left & right respectively
        maxL = height[l]
        maxR = height[r]

        # Output
        res = 0

        # Keep iterating until l & r pointers dont meet
        # TC: O(n)
        while l < r:
            # We always want to consider min between both the maxes
            # This denotes max water that can possibly held in next position
            # The only factor to be considered now is the elevation
            # of that next position.
            if maxL < maxR:
                # l is incremented to next position
                l += 1
                # maxL is the max btwn current max and new position elevation
                # This ensures that if maxL is smaller than new position elevation,
                # the difference isnt negative and just 0.
                maxL = max(maxL, height[l])
                # Compare height of the max elevation yet from left with current one
                res += maxL - height[l]

            else:
                # r pointer decremented to next position
                r -= 1
                # maxR is updated to max until this new position of elevation
                maxR = max(maxR, height[r])
                # Compare height of the max elevation yet from right with current one
                res += maxR - height[r]
        return res
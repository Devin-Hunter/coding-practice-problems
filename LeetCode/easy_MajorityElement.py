"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        """
        This method works, but it isn't linear time, so it's a little slow.
        """
        for num in nums:
            if nums.count(num) > len(nums)/2:
                return num

        """
        This method failed one of the test cases (it was a LONG list of 1s, 2s, & 3s) - it failed for time limit exceeded
        """
        # majority = 0
        # count = 0

        # for n in nums:
        #     if nums.count(n) > count:
        #         majority = n
        #         count = nums.count(n)

        # return majority

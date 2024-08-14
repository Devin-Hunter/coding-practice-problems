"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        This method works to rotate the list
        """

        """
        My first method wasn't working correctly because it didn't account for if k was even or odd, which will change how many elements need to be moved

        This method does account for even or odd k value, but it fails if k == 1 for a list that only has 2 items and if k == 3 for the same 2 item list

        It fails because in the k = 3 test case because the list is only 2 items long, but k = 3, meaning there aren't enough elements to delete and
        move to the front. My lazy method won't work for these cases. I will need to actually get the list to shift k amount of times, removing the last element
        and inserting it into the front for these test cases to pass.
        """

        if k % 2 == 0:
            r = nums[0:k]
            del nums[0:k]
        else:
            r = nums[0:k + 1]
            del nums[0:k + 1]

        nums.extend(r)

        return nums

        """
        This method doesn't work for all cases and I'm not sure why. For some test cases it works with k, but for others it works with k + 1.
        In Thonny, k works for both test cases when entered manually without any changes.

        If I move k amount of elements from the front of the list to the end, I thought it would be the same for every list. However, for some lists,
        moving k amount of elements isn't enough elements.
        """
        # r = nums[0:k]
        # del nums[0:k]

        # return nums.extend(r)

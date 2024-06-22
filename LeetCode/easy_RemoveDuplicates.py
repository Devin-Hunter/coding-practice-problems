"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums. Return k.


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Use a Dictionary:
        # dictionary, key is integer from an array if it doesn't already exist, value is counter
        # if counter is higher than 1, remove from array
        # **** This method best if array/list is NOT sorted ****

        # Use a Pointer:
        # Iterate thru list with for loop, for each int, use pointer to check the number after it, if they are equal,
        # move pointer over 1 position, delete old pointer
        # rinse and repeate until pointer does not equal int
        # **** This method works since array/list IS sorted ****


        next = 1

        for val in nums:
            if next <= len(nums) - 1:
                while next < len(nums) and val == nums[next]:
                    nums.pop(next)
                next += 1

        return len(nums)





    nums = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicates(nums))

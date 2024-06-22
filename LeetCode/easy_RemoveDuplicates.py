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

        ### This method is O(n log n) time, O(n) space. Since sets aren't sorted by nature, we need the sorted function to pass the test. Also, it needed to be
        ###     set to nums[:] to ensure the set was created within the original list, removing all previous contents, therefore removing all duplicates in place
        ###     This method was the fastest of all my solutions***
        nums[:] = sorted(set(nums))
        return len(nums)

        ### This method is O(n^2) time, O(1) space
        # for val in nums:
        #     del nums[nums.index(val):nums.index(val) + (nums.count(val) - 1)]

        # return len(nums)

        ### This method is O(n^2) time, O(1) space

        # current = 0
        # k = 1

        # while current + 1 < len(nums):
        #     count = nums.count(nums[current])
        #     if count > 1:
        #         del nums[current:current + (count - 1)]
        #     else:
        #         current += 1
        #         k += 1

        # return k



        ### This method O(n^2) time complexity, O(1) space complexity

        # next = 1

        # for val in nums:
        #     if next <= len(nums) - 1:
        #         while next < len(nums) and val == nums[next]:
        #             nums.pop(next)
        #         next += 1

        # return len(nums)




        ### This method slighly slower with a O(n^2) time complexity, O(1) space complexity

        # current = 0
        # k = 1

        # while current + 1 < len(nums):
        #     if nums[current] == nums[current + 1]:
        #         nums.remove(nums[current + 1])
        #     else:
        #         current += 1
        #         k += 1

        # return k





    nums = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicates(nums))

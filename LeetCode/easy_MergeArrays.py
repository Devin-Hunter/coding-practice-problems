"""
Problem Description

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # merge the 2 lists, sort it
        # add m & n, if length of list is greater than m + n, remove zeros until length = m + n

        #just use list.remove(0) until enough zeros are removed so that the length of the list = m + n

        for num in nums2:
            nums1.append(num)

        nums1.sort()

        total = (m + n)
        length = len(nums1)

        while length > total:
            nums1.remove(0)
            length = len(nums1)

        return nums1

    # This solution WORKS!! A little slow, but it passes all 59 test cases

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for num in nums2:
            if num > 0 or num < 0:
                nums1.append(num)
        nums1.sort()
        for n in nums1:
            if n <= 0:
                nums1.remove(n)

        # this doesn't remove the last 0. the indexes are off leaving behind the last 0

    def merger(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for num in nums2:
            if num > 0 or num < 0:
                nums1.append(num)

        nums1 = list(filter(lambda a: a != 0, nums1))

        return sorted(nums1)

        # this works locally, but not in the leetcode compiler

"""
Test Case

Input
nums1 =
[1,2,3,0,0,0]
m =
3
nums2 =
[2,5,6]
n =
3

Expected
[1,2,2,3,5,6]
"""


"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores.

Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array A[] of n integers each separated by a space.

Constraints

* 2 <= n <= 10
* -100 <= A[i] <= 100

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # list already exists
    # get the 2nd highest number
        # sort list
        # set index 0 to variable
        # iterate list until 1st num != index 0
        # ***This method was too complex ***


    # s = sorted(arr, reverse=True)

    # first = s[0]

    # for num in s:
    #     if num == first:
    #         s.remove(num)
    # print(s[0])
    # DID NOT WORK

    # for num in s:
    #     while num == first:
    #         s.remove(num)
    # print(s[0])
    # DID NOT WORK




    # list already exists
    # get the 2nd highest number
        # sort list
        # list.count counts how many times the largest number appears, print index of
        # list.count + 1
        # *** This method much simpler and only iterates 1 time for the sort function ***

    sorted_list = sorted(arr, reverse=True)

    i = sorted_list.count(sorted_list[0])
    print(sorted_list[i])

"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal 1+5+9 = 15. The right to left diagonal 3+5+9 = 17. Their absolute difference
is |15 - 17| = 2.

Function description

Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

Constraints

* -100 <= arr[i][j] <= 100

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
"""

def diagonalDifference(arr):
    # Write your code here
    # The first and last rows will always be first[0] and last[length - 1]
    # The middle number(s) will increase 1 row and 1 column until the last row, and reverse
    # for the 2nd diagonal

    matrixSize = len(arr) - 1

    leftDiagonal = 0
    rightDiagonal = 0

    leftfirst = arr[0][0]
    rightfirst = arr[0][matrixSize]

    leftlast = arr[matrixSize][matrixSize]
    rightlast = arr[matrixSize][0]


    final = abs(leftDiagonal - rightDiagonal)

    return final

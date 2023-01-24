#!/bin/python3


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_value = float('-inf')
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if len(arr[x]) - 1 < y + 2:
                continue
            if len(arr) - 1 < x + 2:
                continue
            value = (arr[x][y] + arr[x][y + 1] + arr[x][y + 2])
            value += (arr[x + 1][y + 1] + arr[x + 2][y + 1])
            value += (arr[x + 2][y] + arr[x + 2][y + 2])
            if value > max_value:
                max_value = value

    return max_value


if __name__ == '__main__':

    arr = [
        [-1, - 1, 0, - 9, - 2, - 2, ],
        [- 2, - 1, - 6, - 8, - 2, - 5, ],
        [- 1, - 1, - 1, - 2, - 3, - 4, ],
        [- 1, - 9, - 2, - 4, - 4, - 5, ],
        [- 7, - 3, - 3, - 2, - 9, - 9, ],
        [- 1, - 3, - 1, - 2, - 4, - 5, ]
    ]

    result = hourglassSum(arr)
    print(result)

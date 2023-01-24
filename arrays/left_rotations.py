#!/bin/python3

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


def rotLeft(a, d):
    # Write your code here
    [arr_len, rotations] = a.split(' ')
    print(arr_len, rotations)
    arr = d.split(' ')
    print(arr)
    result_b = ''
    result_a = ''
    for x in range(len(arr)):
        if x >= int(rotations):
            result_b = f'{result_b}{arr[x]} '
        else:
            result_a = f'{result_a}{arr[x]} '

    return (result_b.strip() + ' ' + result_a.strip())


if __name__ == '__main__':

    result = rotLeft(
        '20 10', '41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51')
    print(result)

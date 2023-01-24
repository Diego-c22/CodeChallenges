
def swap(arr: list, index1: int, index2: int) -> list:
    temp: int = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps: int = 0
    for i in range(len(arr)):
        if (len(arr) > i + 1 and arr[i] != i + 1):
            while arr[i] != i + 1:
                swap(arr, i, arr[i] - 1)
                swaps += 1
    return swaps
                
                
if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 6, 7]
    res = minimumSwaps(arr)
    print(res)

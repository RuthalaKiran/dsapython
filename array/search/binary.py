#  implement binary search


def binarySearch(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle + 1
        elif arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return -1

# tc - O(logn)

arr = [1, 2, 3, 4, 5]
print(binarySearch(arr, 5))

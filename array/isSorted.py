#  check if the array is sorted

def isSorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] >= arr[i-1]: continue
        else:
            return False
    return True

# tc - O(n)

arr = [1,2,3,4]
print(isSorted(arr))
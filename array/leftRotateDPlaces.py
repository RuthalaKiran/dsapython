# left rotate the array by d places


# bruteforce
def leftRotateBrute(arr, d):
    n = len(arr)
    d = d % n
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(d, n):
        arr[i - d] = arr[i]
    j = 0
    for i in range(n - d, n):
        arr[i] = temp[j]
        j += 1


# tc - O(d) + O(n-d) + O(d) = O(n+d)
# sc - O(d)


def leftRotateOptimal(arr, d):
    n = len(arr)
    reverse(0, d - 1, arr)
    reverse(d, n - 1, arr)
    reverse(0, n - 1, arr)

def reverse(low, high, arr):
    while low <= high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

# tc - O(2n)
# sc - O(1)

arr = [1, 2, 3, 4, 5, 6, 7]
d = 1
print(leftRotateOptimal(arr, d))
print(arr)

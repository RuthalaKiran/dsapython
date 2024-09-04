#  sort an array of 0 1 2

# brute force
# merge or quick sort


# better
def sort012Better(arr):
    n = len(arr)
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    i = 0
    while cnt0:
        arr[i] = 0
        i += 1
        cnt0 -= 1
    while cnt1:
        arr[i] = 1
        i += 1
        cnt1 -= 1
    while cnt2:
        arr[i] = 2
        i += 1
        cnt2 -= 1
    return cnt0, cnt1, cnt2


# tc - O(2n)


# optimal dutch national flag algorithm
def Sort012Optimal(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[high]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


# tc - o(n)

arr = [0, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0]
print(Sort012Optimal(arr))
print(arr)

# dutch national flag algorithm
# [0...low-1] --> 0 extreme left
# [low...mid-1] --> 1
# [high+1...n-1] --> 2
#
#
#
#

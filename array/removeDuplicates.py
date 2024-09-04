# remove duplicates in an array in-place from sorted array

# brute force
def removeDuplicatesBrute(arr):
    n = len(arr)
    myset = list(set(arr))
    for i in range(len(myset)):
        arr[i] = myset[i]
    return len(myset)
    
# tc - O(n)
# sc - O(n)


# optimal approch
def removeDuplicatesOptimal(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i +=1
    return i+1

# tc - O(n)

arr = [1,1,2,2,2,3,3]
print(removeDuplicatesOptimal(arr))
print(arr)
# linear search

def linearSearch(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i+1
    return -1

# tc - O(n)

arr = [6,7,8,4,1]
print(linearSearch(arr,1))
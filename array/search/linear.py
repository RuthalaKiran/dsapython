#  implement linear search

def linear(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i+1
    return -1

# tc - O(n)

arr = [1,2,3,4,5]
print(linear(arr,5))
# return largest element in an arry

# brute force 
def largestBrute(arr):
    n = len(arr)
    arr.sort()        
    return arr[n-1]

# tc - O(nlogn)

# optimal
def largestoptimal(arr):
    n = len(arr)
    large = arr[0]
    for i in range(1,n):
        if arr[i] > large:
            large = arr[i]
    return large

# tc - O(n)

arr = [3,2,1,5,2]
print(largestoptimal(arr))
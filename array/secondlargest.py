# return second largest element in an array

# bruteforce
def SlargestBrute(arr):
    n = len(arr)
    arr.sort()
    largest = arr[n-1]
    secondlargest = -1
    for i in range(n-2,-1,-1):
        if arr[i] != largest:
            secondlargest = arr[i]
            break
    return secondlargest

# tc - O(nlogn + n)


# better approch
def SlargestBetter(arr):
    n = len(arr)
    large = arr[0]
    for i in range(n):
        if arr[i]>large:
            large = arr[i]
    secondlarge = -1
    for i in range(n):
        if arr[i] > secondlarge and arr[i] != large:
            secondlarge = arr[i]
    return secondlarge

# tc - O(2n)

# optimal approch

def SlargestOptimal(arr):
    n = len(arr)
    large = arr[0]
    secondlarge = -1
    for i in range(n):
        if arr[i] > large :
            secondlarge = large
            large = arr[i]
        if arr[i] <large and arr[i] > secondlarge:
            secondlarge = arr[i]
    return secondlarge  

# tc - O(n)

arr = [1,2,4,7,7,5]
print(SlargestOptimal(arr))
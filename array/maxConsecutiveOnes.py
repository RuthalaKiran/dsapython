#  maximum consecutive ones

def consecutiveOnes(arr):
    n = len(arr)
    count = 0
    maxcount = 0
    for i in range(n):
        if arr[i] == 1:
            count +=1
            maxcount = max(maxcount,count)
        else:
            count = 0
    return count

arr = [1,1,0,1,1,1]
print(consecutiveOnes(arr))
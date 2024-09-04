def maximun(arr):
    maxi = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[maxi]:
            maxi = i
    return arr[maxi],maxi


print(maximun([1, 2, 3, 4, 5]))

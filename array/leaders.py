# leaders in an array


# brute force
def leaderBrute(arr):
    n = len(arr)
    res = []
    for i in range(n):
        leader = True
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader == True:
            res.append(arr[i])
    return res


# tc - O(n^2)
# sc - O(leaders)


# optimal
def leaderOptimal(arr):
    n = len(arr)
    maxi = -1
    ans = []
    for i in range(n - 1, -1, -1):
        if arr[i] > maxi:
            ans.append(arr[i])
        maxi = max(maxi, arr[i])
    return ans

# tc - O(n)
# sc - O(leaders)

arr = [10, 22, 12, 3, 0, 6]
print(leaderBrute(arr))

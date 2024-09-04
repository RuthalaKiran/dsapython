#  Four Sum


# brute force
def FourSumBrute(arr, target):
    n = len(arr)
    myset = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    sum = arr[i] + arr[j] + arr[k] + arr[l]
                    if sum == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        myset.add(tuple(temp))

    ans = [list(item) for item in myset]
    return ans


# tc - O(n^4)
# sc - O(2*no. of quards)


# better
def FourSumBettr(arr, target):
    n = len(arr)
    myset = set()
    for i in range(n):
        for j in range(i + 1, n):
            hashmap = set()
            for k in range(j + 1, n):
                summ = arr[i] + arr[j] + arr[j]
                fourth = target - (summ)
                if fourth in hashmap:
                    temp = [arr[i], arr[j], arr[k], fourth]
                    temp.sort()
                    myset.add(tuple(temp))
                hashmap.add(arr[k])
    ans = [list(item) for item in myset]
    return ans


# tc - O(n^3)
# sc - O(2*no. of quards) + O(n)


# optimal
def FourSumOptimal(arr, target):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, n):
            if j != i + 1 and arr[j] == arr[j - 1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    ans.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                    while k < l and arr[l] == arr[l - 1]:
                        l -= 1
                elif sum < target:
                    k += 1
                else:
                    l -= 1
    return ans

# tc - O(n^3) 
# sc - O(no. of quards)

arr = [1, 0, -1, 0, -2, 2]
print(FourSumOptimal(arr, 0))

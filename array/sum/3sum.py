# Three Sum


# bruteforce
def ThreeSumBrute(arr):
    n = len(arr)
    myset = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    myset.add(tuple(temp))
    ans = [list(item) for item in myset]
    return ans


# tc - O(n^3) + O(n)
# sc - O(2*no. of triplets)


# better approch
def ThreeSumBetter(arr):
    n = len(arr)
    myset = set()
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                myset.add(tuple(temp))
            hashset.add(arr[j])
    ans = [list(item) for item in myset]
    return ans


# tc - O(n^2) + O(nlogn)
# sc - O(n) + O(no. of unique triplets)


# optimal approch
def ThreeSumOptimal(arr):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                ans.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k - 1]:
                    k -= 1
    return ans


# tc - O(n^2) + O(nlogn)
# sc - O(no. of triplets)

arr = [-2, 0, 1, 1, 2]
print(ThreeSumOptimal(arr))

# unio of two sorted arrays


# brute force
def unionBrute(arr1, arr2):
    myset = list(set(arr1 + arr2))
    return myset


# tc - O(n1+n2+n)
# sc - O(n1+n2)


# optimal approch
def unionOptimal(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    res = []
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            if arr1[i] not in res:
                res.append(arr1[i])
            i += 1
        else:
            if arr2[j] not in res:
                res.append(arr2[j])
            j += 1
    while i < n1:
        if arr1[i] not in res:
            res.append(arr1[i])
        i += 1
    while j < n2:
        if arr2[j] not in res:
            res.append(arr2[j])
        j += 1
    return res

# tc - O(n1+n2)
# sc - O(n1+n2)

arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
print(unionOptimal(arr1, arr2))

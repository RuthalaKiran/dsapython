# intersection of two sorted arrays


# brute force
def intersection(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    vis = [0] * n2
    ans = []
    for i in range(n1):
        for j in range(n2):
            if arr1[i] == arr2[j] and vis[j] == 0:
                ans.append(arr1[i])
                vis[j] = 1
                break
            if arr2[j] > arr1[i]:
                break
    return ans


# tc - O(n2)
# sc - O(n2) + O(no. of unique elements)


# optimal aproch
def intersectionOptimal(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    ans = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
            j += 1
    return ans


# tc - O(n1+n2)
# sc - O(n)

arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
print(intersectionOptimal(arr1, arr2))

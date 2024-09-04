#  merge 2 sorted arrays without extra space

# brute force
def mergeBrute(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    l = 0
    r = 0
    temp = []
    while l < n1 and r < n2:
        if arr1[l] <= arr2[r]:
            temp.append(arr1[l])
            l += 1
        else:
            temp.append(arr2[r])
            r += 1
    while l < n1:
        temp.append(arr1[l])
        l += 1
    while r < n2:
        temp.append(arr2[r])
        r += 1
    for i in range(0, n1 + n2):
        if i < n1:
            arr1[i] = temp[i]
        else:
            arr2[i - n1] = temp[i]

# tc - O(n1+n2) + O(n1+n2)
# sc - O(n1 + n2)


# optimal
def mergeOptimal(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    l = n1 - 1
    r = 0
    while l>=0 and r <n2:
        if arr1[l] > arr2[r]:
            arr1[l],arr2[r] = arr2[r],arr1[l]
            l -= 1
            r += 1
        else:
            break
    arr1.sort()       
    arr2.sort()  

# tc - O(min(n1,n2)) + O(n1logn1) + O(n2logn2)

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(mergeOptimal(arr1, arr2))
print(arr1 + arr2)

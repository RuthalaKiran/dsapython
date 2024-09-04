def kth_largest(arr, k):
    for i in range(k):
        maxindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[maxindex]:
                maxindex = j
        arr[i], arr[maxindex] = arr[maxindex], arr[i]
    return arr[k - 1]


print(kth_largest([1, 2, 3, 4, 5], 1)) 


# tc - O(k*n)
# sc - O(1)

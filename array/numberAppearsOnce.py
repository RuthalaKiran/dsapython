# find the number that appears once , and the others twice


# brute force
def Once(arr):
    n = len(arr)
    for i in range(n):
        num = arr[i]
        cnt = 0
        for j in range(n):
            if arr[j] == num:
                cnt += 1
        if cnt == 1:
            return num


# tc - O(n^2)


# better approch
def OnceBetter(arr):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        if arr[i] in hashmap:
            hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
        else:
            hashmap[arr[i]] = 1
    for key, val in hashmap.items():
        if val == 1:
            return key

# tc - O(2n)
# sc - O(n)

# optimal approch
def OnceOptimal(arr):
    n = len(arr)
    xor  = 0
    for i in range(n):
        xor ^= arr[i]
    return xor

arr = [1, 1, 2, 3, 3, 4, 4]
print(OnceOptimal(arr))

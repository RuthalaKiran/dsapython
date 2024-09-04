# find the missing number


# brute force
def missingNoBrute(arr):
    n = len(arr)
    for i in range(n + 1):
        flag = 0
        for j in range(n):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i


# tc - O(n^2)


# better approch
def missingNoBetter(arr):
    n = len(arr)
    hashmap = [0] * (n + 1)
    for i in range(n):
        hashmap[arr[i]] = 1
    for i in range(n):
        if hashmap[i] == 0:
            return i


# tc - O(2n)
# sc - O(n)


# optimal approch
# 1.Sum
def summing(arr):
    n = len(arr)
    arraysum = sum(arr)
    sumn = (n * (n + 1)) // 2
    return sumn - arraysum


#  tc - O(n)


# 2.XOR
def xoring(arr):
    n = len(arr)
    xor1 = 0
    xor2 = 0
    for i in range(n):
        xor1 = xor1 ^ i
        xor2 = xor2 ^ arr[i]
    xor1 = xor1 ^ n
    return xor1 ^ xor2

# tc - O(n)

arr = [9,6,4,2,3,5,7,0,1]
print(xoring(arr))

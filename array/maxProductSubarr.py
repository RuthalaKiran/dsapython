#  maximum product subarray

# brute force


def maxProductBrute(arr):
    n = len(arr)
    maxi = 0
    maxproduct = float("-inf")
    for i in range(n):
        for j in range(i+1, n+1):
            product = 1
            for k in range(i, j):
                product = product * arr[k]
            maxi = max(maxi, j - i + 1)
            maxproduct = max(product, maxproduct)
    return maxproduct


# tc - O(n^3)


# better
def maxProductBetter(arr):
    n = len(arr)
    maxi = 0
    maxproduct = float("-inf")
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod = prod * arr[j]
            maxproduct = max(prod, maxproduct)
    return maxproduct

# tc - O(n^2)


# optimal
def maxProductOptimal(arr):
    n = len(arr)
    ans = float("-inf")
    pre = 1
    suf = 1
    for i in range(n):
        if pre == 0 : pre = 1
        if suf == 0 : suf = 1
        pre = pre * arr[i]
        suf = suf * arr[n-i-1]
        ans = max(ans,max(pre,suf))
    return ans
        
# tc - O(n)

nums = [2, 1, -1]
print(maxProductOptimal(nums))

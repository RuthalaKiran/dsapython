# count the subarray with sum k


# better
def subarraySum( nums, k):
    n = len(nums)
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                cnt += 1
    return cnt

# tc - O(n^2)

#  optimal

nums = [1,1,1]
k = 2
print(subarraySum(nums,k))

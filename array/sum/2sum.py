#  Two Sum


# brute force
def TwoSumBrute(arr, target):
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            if arr[i] + arr[j] == target:
                # return i,j
                return "yes"
    return "no"


# tc - O(n^2)


# better approch
def TwoSumBetter(arr, target):
    n = len(arr)
    mpp = {}
    for i in range(n):
        num = arr[i]
        more = target - num
        if more in mpp:
            # return i,mpp[more]
            return "yes"
        mpp[num] = i
    return "no"


# tc - O(n)
# sc - O(n)


# Optimal aproch
def TwoSumOptimal( nums, target):
    n = len(nums)
    nums.sort()
    left = 0
    right = n - 1
    while left <= right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

# tc - O(n) + O(nlogn)

arr = [2, 6, 5, 8, 11]
print(TwoSumOptimal(arr, 13))

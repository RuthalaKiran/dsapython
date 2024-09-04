#  majority element


# better 
def majorityElementBeter(v):
    n = len(v)
    mpp = {}
    for num in v:
        if num in mpp:
            mpp[num] += 1
        else:
            mpp[num] = 1
    temp = []
    for key, val in mpp.items():
        if val > n // 3:
            temp.append(key)
    temp.sort()
    return temp

# tc - O(2n) + O(nlogn)
# sc - O(n)

arr = [1, 1, 1, 2, 2, 2]
print(majorityElementBeter(arr))

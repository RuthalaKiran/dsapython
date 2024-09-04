# move all zeros to the end of th array


# bruteforce
def moveZerosBrute(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i] = temp[i]
    length = len(temp)
    for i in range(length, n):
        arr[i] = 0


# tc - O(n) + O(x) + O(n-x) = O(2n)
# sc - O(x)


# optimal approch
def moveZerosOptimal(arr):
    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

# tc - O(x) + O(n-x) = O(n)

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
print(moveZerosOptimal(arr))
print(arr)

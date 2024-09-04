# find the largest number that can be formed with the given digits

# input - [3,30,34,5,9]
# output - 9534330


def largestwithdigits(arr):
    n = len(arr)
    largestnum = ""
    for i in range(n):
        for j in range(i + 1, n):
            temp1 = str(arr[i]) + str(arr[j])
            temp2 = str(arr[j]) + str(arr[i])
            if int(temp2) > int(temp1):
                arr[i], arr[j] = arr[j], arr[i]
    for i in range(n):
        largestnum += str(arr[i]) 
    print(largestnum)


largestwithdigits([3, 30, 34, 5, 9])

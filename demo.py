from collections import Counter

char = "5"
print(char.isdigit())

char = "a"
print(char.isalpha())

char = "@"
print(char.isalnum())


def countSeniors(details):
    n = len(details)
    temp = []
    for i in range(n):
        agearr = details[i][11:13]
        res = "".join(agearr)
        temp.append(res)
    count = 0
    for i in range(len(temp)):
        if int(temp[i]) > 60:
            count += 1
    return count


details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(countSeniors(details))

s = "Kiran"
s = s.lower()
print(s)
s = "anagram"
t = "nagaram"


def validanagram(s, t):
    s1 = len(s)
    s2 = len(t)
    if s1 != s2:
        return False
    str1 = sorted(s)
    str2 = sorted(t)
    str1.sort()
    str2.sort()
    if str1 == str2:
        return True
    return False


print(validanagram(s, t))


arr = [3, 7, 9]
target = [3, 7, 11]
arr.sort()
target.sort()
print(arr == target)
print(Counter(arr))
count1 = {}
count2 = {}
for n1, n2 in zip(target, arr):
    if n1 in count1:
        count1[n1] += 1
    else:
        count1[n1] = 1
    if n2 in count2:
        count2[n2] += 1
    else:
        count2[n2] = 1
print(len(count1), len(count2))
print(count1, count2)
for n in count1:
    if count1[n] != count2.get(n):
        print(False)


def winningPlayerCount(n, pick):
    player_pick = {i: {} for i in range(n)}

    for player, color in pick:
        if color in player_pick[player]:
            player_pick[player][color] += 1
        else:
            player_pick[player][color] = 1
    winner = 0
    for player in range(n):
        max_balls = max(player_pick[player].values(), default=0)
        if max_balls > player:
            winner += 1
    return winner


n = 4
pick = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
print(winningPlayerCount(n, pick))


def rangeSum(nums, n, left, right):
    temp = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = sum + nums[j]
            temp.append(sum)
    temp.sort()
    sum = 0
    for i in range(left - 1, right):
        sum = sum + temp[i]
        print(i)
    return sum


nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
print(rangeSum(nums, n, left, right))


def max_zeros_II(arr):
    length = 0
    n = len(arr)
    for i in range(n):
        zeorscnt = 0
        for j in range(i, n):
            if arr[j] == 0:
                zeorscnt += 1
            if zeorscnt <= 1:
                length = max(length, j - i + 1)
            else:
                break
    return length


def max_zeros_IIoptimal(arr):
    n = len(arr)
    maxlen = 0
    l = 0
    r = 0
    zeros = 0
    while r < n:
        if arr[r] == 0:
            zeros += 1
        while zeros > 1:
            if arr[l] == 0:
                zeros -= 1
            l += 1
        if zeros <= 1:
            maxlen = max(maxlen, r - l + 1)
        r += 1
    return maxlen


arr = [1, 0, 1, 1, 0]
print(max_zeros_IIoptimal(arr))


def unique(arr):
    count = Counter(arr)
    occurences = set()
    
    for val in count.values():
        if val in occurences:
            return False
        occurences.add(val)
    return True

arr = [1,2,2,1,1,3]
print(unique(arr))

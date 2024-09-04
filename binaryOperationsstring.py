def binaryoperation(s1,s2,operation):
    ans = ''
    if operation == "AND":
        for i in range(len(s1)):
            if s1[i] == '1' and s2[i] == '1':
                ans = ans + '1'
            else:
                ans = ans + "0"
    if operation == "OR":
        for i in range(len(s1)):
            if s1[i] == '1' or s2[i] == '1':
                ans = ans + '1'
            else:
                ans = ans + "0"
    if operation == "XOR":
        for i in range(len(s1)):
            if s1[i] == '1' and s2[i] == '1':
                ans = ans + '0'
            elif s1[i] == '0' and s2[i] == '0':
                ans = ans + '0'
            else:
                ans = ans + "1"
    return ans
s1 = '1101'
s2 = '1011'
op = 'XOR'
print(binaryoperation(s1,s2,op))
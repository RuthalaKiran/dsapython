def changechar(s, ch1, ch2):
    n = len(s)
    res = ""
    for i in range(n):
        if s[i] == ch1:
            res += ch2
        elif s[i] == ch2:
            res += ch1
        else:
            res += s[i]
    return res


s = "hello world"
ch1 = "h"
ch2 = "w"
print(changechar(s, ch1, ch2))

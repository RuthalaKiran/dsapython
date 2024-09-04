def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    sortedstring1 = sorted(s1)
    sortedstring2 = sorted(s2)
    if sortedstring1 == sortedstring2:
        return True
    return False


s1 = "listen"
s2 = "silent"
print(anagram(s1, s2))

print(sorted(s1))

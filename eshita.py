def cancreate(a, b):
    ransom = {}
    magazine = {}
    for i in a:
        ransom[i] = ransom.get(i, 0) + 1
    for i in b:
        magazine[i] = magazine.get(i, 0) + 1
    for i in ransom.keys():
        if i not in magazine.keys():
            return False
        if ransom[i] > magazine[i]:
            return False
    return True


print(cancreate("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))

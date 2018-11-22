def pattern_hunting(l1, l2, p):
    result = []
    for x in l1:
        if p in x:
            result.append(l2[l1.index(x)])
    for x in l2:
        if p in x:
            result.append(l1[l2.index(x)])
    a = sorted(result)
    return a[::-1]
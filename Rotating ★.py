def rotate_list(l):
    for x in range(3):
        a = l.pop(0)
        l.append(a)
    return l
def unpack_rev(atuple):
    a = []
    for x in atuple:
        a.append(x)
    a = a[::-1]
    a = " ".join(a)
    return a
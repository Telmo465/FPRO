def fetch_middle(lists):
    result = []
    for x in lists:
        if len(x) % 2 != 0:
            result.append(x[int(len(x)/2)])
        if len(x) % 2 == 0:
            a = (len(x)//2)-1
            b = (len(x)//2 + 1)-1
            c = (x[a]+x[b])/2
            result.append(c)
    return result
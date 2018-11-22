def add_item(tup, idx, item):
    l = list(tup)
    if len(tup) == 0:
        l.insert(0,item)
    if idx == 0 or idx == -(len(tup)):
        l[idx] = item
    elif idx == (len(l)-1) or idx == -1:
        l[idx] = item
    else:
        l.insert(idx,item)
    return(tuple(l))
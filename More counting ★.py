def count_elems(tup):
    result = ()
    for x in tup:
        if type(x) == tuple or type(x) == list or type(x) == str:
            result += (len(x),)
        else:
            result +=(1,)
    return result
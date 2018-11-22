def summary(text):
    result = ()
    count = 0
    result +=(len(text.split()),)
    a = text.upper()
    a = a.split(" ")
    for x in a:
        if "E" in x:
            count += 1
    result += (count,)
    return result

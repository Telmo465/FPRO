def count_until(tup):
    count = 0
    for x in tup:
        if type(x).__name__ != "tuple":
            count += 1
        elif type(x).__name__ == "tuple":
            break
    else:
        count = -1
    return count
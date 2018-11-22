def longest(s):
    current_max = 0
    words = s.split()
    for i in words:
        if len(i) > current_max:
            current_max = len(i)
    return current_max
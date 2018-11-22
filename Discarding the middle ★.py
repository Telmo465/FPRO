def discard_middle(s):
    if (len(s) <= 3):
        result = ''
    else:
        result = s[0:2]+s[(len(s)-2):(len(s))]
    return result
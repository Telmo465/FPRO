def summary_ranges(astring):
    TAG = 0
    res = []
    astring = astring.split(",")
    astring.append(-1)
    for i in range(len(astring)):
        if i > 0:
            if (int(astring[i]) - int(astring[i-1])) == 1 and TAG == 0:
                TAG = 1
                begin = astring[i-1]
            elif int(astring[i]) - int(astring[i-1]) != 1 and TAG == 1:
                TAG = 0
                end = (astring[i-1])
                res.append(begin+'->'+end)
            elif int(astring[i]) - int(astring[i-1]) != 1 and TAG == 0:
                res.append((astring[i-1]))
    res = ','.join(res)
    return res
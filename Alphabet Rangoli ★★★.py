def rangoli(N):
    if N == 1:
        result = "a"
        return result
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = []
    row_list = []
    for r in range(1, N+1):
        row = "-"*(2*N-2*r)
        for c in range(1, r+1):
            letters += [alphabet[N-c]]
        join_let = "-".join(list(reversed(letters)))
        row += "-".join(letters) + join_let[1:] +"-"*(2*N-2*r)
        letters = []
        row_list += [row]
    row_list = row_list + row_list[N-2::-1]
    result = "\n".join(row_list)
    return result
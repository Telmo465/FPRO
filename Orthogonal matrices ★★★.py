def is_orthogonal(mx):
    n = len(mx[0])
    d = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        d[i][i]=1
    transposta = zip(*mx)
    mult = [[sum(a*b for (a,b) in zip(i, j)) for i in mx] for j in zip(*transposta)]
    if mult == d:
        return True
    return False
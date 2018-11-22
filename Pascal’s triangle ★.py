import math

def pascal(n):
    r = n
    result = ""
    for i in range(0,n):
        if i != 0:
            result = str(result) + "\n"
        for j in range(0,r):
            a = i-j
            if a < 0:
                break
            if j == 0:
                result1 = 1
            else:
                result1 = int(math.factorial(i)/(math.factorial(j)*math.factorial(a)))
            result = str(result)+ " " + str(result1)
    return result
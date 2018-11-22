def collatz(n):
    result = ''
    if (n > 0 and (type(n) == int) and n != 1):
        result += (str(n) + ",")
        while n != 1:
            if (n % 2) == 0:
                n = int(n/2)
                if n == 1:
                    result += str(n)
                else:
                    result += (str(n)+ ",")
            elif (n % 2) != 0:
                n = int(n*3+1)
                result += (str(n)+",")
    elif n == 1:
        result += str(n)
    return result
def solver(a,b,c):
    import math
    caralho = []
    d = b**2-4*a*c # discriminant
    if d < 0:
        return caralho
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        caralho.append(x)
        return caralho
    else:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        x = [x1,x2]
        return sorted(x)
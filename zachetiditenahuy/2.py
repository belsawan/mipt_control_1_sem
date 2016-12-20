def f(a):
    return float(a-2)

def bisection(a ,b , eps):
    while b-a>eps:
        c = float((a + b) / 2)
        if f(c) == 0:
            return c
        if f(a)*f(c)<0:
            a,b=a,c
        else:
            a,b=c,b
    return float((b-a)/2)
print(bisection(-1, 100, 0.1))

'''def insection(a,b, eps):
    while abs(b - a) > eps*2:
        c = (a + b)/2
        if f(c)==0:
            return c
        if f(c)*f(a) < 0:
            a,b = a,c
        else:
            a,b=c,b
    return (b-a)//2

print(insection(-1, 6, 0.0001))'''


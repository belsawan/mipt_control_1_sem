def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)


'''def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(5))'''

def fib(n):
    Fib=[0]+[1]+[0]*(n-1)
    print(Fib)
    for i in range(2, n+1):
        Fib[i]=Fib[i-1]+Fib[i-2]
    return Fib[n]

print(fib(5))
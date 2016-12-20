def power(a, n):
    if n==1:
        return a
    return power(a, n-1)*a

def fastpower(a, n):
    if n==0:
        return 1
    if n%2==0:
        return fastpower(a*a, n//2)
    else:
        return fastpower(a, n-1)*a

print(fastpower(2, 4))


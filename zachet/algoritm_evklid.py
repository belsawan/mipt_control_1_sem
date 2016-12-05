def gcd(a,b):
    if a==b:
        return a
    else:
        if a>b:
            print(a - b, b)
            return gcd(a-b,b)
        else:
            print(a - b, b)
            return gcd(a,b-a)
print(gcd(10,12))
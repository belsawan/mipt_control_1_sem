def f(n):
    if n==0:
        print('K')
        return 1
    print('C')
    fn_1 = f(n-1)
    print('O')
    res=fn_1*n
    return res

f(5)

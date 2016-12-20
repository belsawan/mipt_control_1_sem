def upper_found(key, A):
    A = sorted(A)
    l = -1
    r = len(A)
    while r-l > 1:
        m = (l + r)//2
        if A[m] > key:
            r = m
        else:
            l = m
    return r

A=[1,1,1,2,3,5,5,5,5,6,6,6,7,9,21]
print(upper_found(5,A))
def hoar_sort(A):
    if len(A)<=1:
        return A
    barrier=A[0]
    L, M, R=[], [], []
    for i in A:
        if i > barrier:
            R.append(i)
        elif i == barrier:
            M.append(i)
        else:
            L.append(i)
    return hoar_sort(L)+M+hoar_sort(R)

A=[1,3,2,4,1,2]
print(hoar_sort(A))

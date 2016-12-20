def sdviz_pravo(A):
    tmp=A[-1]
    for i in range(len(A)-1, 0, -1):
        A[i]=A[i-1]
    A[0] = tmp

A=[1,2,3,4,5,6,7]


def sdviz_vlevo(A):
    tmp=A[0]
    for i in range(1, len(A)):
        A[i-1]=A[i]
    A[-1]=tmp

sdviz_vlevo(A)
print(A)
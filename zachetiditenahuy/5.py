def bubble_sort(A):
    for i in range(len(A)):
        for j in range(1, len(A)-i):
            if A[j-1]<A[j]:
                A[j-1],A[j]=A[j],A[j-1]
    A[:] = A[::-1]


A=[1,3,2,4,1,2]
bubble_sort(A)
print(A)
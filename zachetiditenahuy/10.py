def merge_sort(A):
    if len(A) <= 1:
        return A[:]
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    return merge(L, R)

def merge(A, B):
    i=j=k=0
    C = [None] * (len(A)+len(B))
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C[k] = A[i]; i += 1; k += 1
        else:
            C[k] = B[j]; j += 1; k += 1
    C[k:] = A[i:] + B[j:]
    return C

A=[1,5, 4, 6, 1 ,4]
merge_sort(A)
print(merge_sort(A))
A = [1, 2, 7, 2, 4]
B = [2, 5, 8, 1 ,4]

def sync_sort(A, B):
    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                B[j], B[j+1] = B[j+1], B[j]
            if A[j] == A[j+1]:
                B[j], B[j+1] = min(B[j], B[j+1]), max(B[j], B[j+1])
    return A, B
print(sync_sort(A, B))
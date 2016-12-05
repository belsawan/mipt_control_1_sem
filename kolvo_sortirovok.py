A = list(map(int, input().split()))
def bubble_sort_perestanovki(A):
    m = 0
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                m += 1
    return m
print(bubble_sort_perestanovki(A))
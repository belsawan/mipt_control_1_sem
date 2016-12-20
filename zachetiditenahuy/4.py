A=[1,3,2,4,1,2]
def choice_sort(A):
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[j]>A[i]:
                A[i],A[j]=A[j], A[i]
    A[:]=A[::-1]

def insertion_sort(A):
    for i in range(1, len(A)):
        tmp = A[i]
        k = i - 1
        while k >= 0 and A[k] > tmp:
            A[k+1] = A[k]
            k -= 1
        A[k+1] = tmp


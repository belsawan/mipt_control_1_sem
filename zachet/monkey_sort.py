from random import shuffle

def sort(A):
    m=0
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            m += 1
    if m == (len(A)-1):
        return True
    else:
        return False

def monkey_sort(A):
    while sort(A) != True:
        shuffle(A)
    return A

a = [2, 1]
print(monkey_sort(a))


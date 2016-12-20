def count_sort (A):
    Q = [0]*10
    for x in A:
        Q[x] += 1
    pos = 0
    for x in range(0,10):
        for i in range(Q[x]):
            A[pos] = x
            pos += 1
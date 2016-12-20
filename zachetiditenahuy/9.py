def radix_sort(A):
    for k in range(3):
        B = [[] for i in range(10)]
        for x in A:
            digit = (x // 10 ** k) % 10
            B[digit].append(x)
        A[:] = []
        for digit in range(10):
            A.extend(B[digit])

A=[1,10,347, 345,10, 513, 122, 39, 25, 48]
radix_sort(A)
print(A)

A = ['hleb', 'chai', 'sahar', 'hleb', 'chai', 'sahar','maslo','hleb']
m = []
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] != A[j]:
            continue
        elif A[j] in m:
            break
        else:
            m.append(A[j])
print(*m)

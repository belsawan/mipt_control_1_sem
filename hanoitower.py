def hanoi(n,i=1,k=2):
    if n == 1:
        print('переложить блин 1 с ', i,' на ', k)
    else:
        tmp = 6-i-k
        hanoi(n-1, i, tmp)
        print('переслать блин', n,'c', i,'на', k)
        hanoi(n-1, tmp, k)

N=int(input())
hanoi(N)
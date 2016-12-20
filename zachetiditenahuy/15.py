def hanoi(n, i=1, k=2):
    if n == 1:
        print('Переложить блин 1 с', i, 'на', k)
    else:
        tmp=6-i-k
        hanoi(n-1, i, tmp)
        print('Переложить блин',  n, 'с', i, 'на', k)
        hanoi(n-1, tmp, k)

hanoi(4)
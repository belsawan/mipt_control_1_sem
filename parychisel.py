# Ввод массива
# Если способ работать без n?
n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split(' ')])
# Проверка пар и их вывод
for u in range(len(a)):
        m = 0
        if a[u][m] == 0 and a[u][m+1] == 0:
            break
        else:
            if a[u][m] % 2 == 0 and a[u][m+1] % 7 == 0:
                if a[u][m] > 99 or a[u][m+1] > 99:
                    print(str(a[u][m])+' '+str(a[u][m+1]))


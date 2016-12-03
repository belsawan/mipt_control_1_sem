# Задание списка
A = list(map(int, input().split()))
# Нахождение максимума
n = 0
s = 0
for i in A:
    if i == 0:
        break
    if i > s:
        s = i
for j in A:
    if j == 0:
        break
    if j == s:
        n += 1
print(n)
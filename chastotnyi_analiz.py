def spisok(N):
    a = []
    for i in range(N):
         a.append(input())
    return a

def analiz(L):
    b = []
    for i in L:
        s=0
        for j in L:
            if j == i:
                s += 1
        b.append(s)
    return b
# TODO нужно разобраться со списком; он выдаёт все номера для каждого товара

"""def proverka(b):
    m=0
    for i in b:
        for"""
    # FIXME make me work and to do main quest


N=int(input())
a=spisok(N)
print(analiz(a))

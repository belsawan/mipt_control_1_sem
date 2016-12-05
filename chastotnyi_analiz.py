def spisok(N):
    a = []
    for i in range(N):
         a.append(input())
    return a

def spisok_poodinochke(L):
    m = []
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] != L[j]:
                continue
            elif L[j] in m:
                break
            else:
                m.append(L[j])
    return m
def analiz(L):
    m = spisok_poodinochke(L)
    b = []
    for u in m:
        s = 0
        for y in L:
            if u == y:
                s += 1
        b.append(s)
    return b
'''def proverka(L):
    b = analiz(L)
    m = spisok_poodinochke(L)
    for i in range(10):
        u = b.count(i)
        if u > 0:
            for j in range(u):
                tmp = b.index(u)
                b.pop(tmp)
                print(m[tmp])'''


# FIXME без словарей трудна!


N = int(input())
a = spisok(N)
print(spisok_poodinochke(a))
print(analiz(a))

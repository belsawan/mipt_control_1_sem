def spisok(N):
    a = []
    for i in range(N):
         a.append(input())
    return a

def spisok_poodinochke(L):
    m = []
    b = []
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
    b=[]
    for u in m:
        s=0
        for y in L:
            if u == y:
                s += 1
        b.append(s)
    return b

'''def proverka(b):
    m = 0
    for i in b:
        for'''
# FIXME осталось только самый конец доделать, я курить пошёл


N = int(input())
a = spisok(N)
print(spisok_poodinochke(a))
print(analiz(a))
'''asdasd'''

def check_and_do_properly(A):
  c = ord('A')
  for i in range(len(A)):
    if A[i] >= 10:
      A[i] = chr(A[i] - 10 + c)
  return A

def perevod(chislo, base):
  A = []
  while chislo > 0:
    A.append(chislo % base)
    chislo = chislo // base
  A = A[::-1]
  A = check_and_do_properly(A)
  s = ''
  for i in A:
    s += str(i)
  return s

def perevod_any(chislo, base1, base2):
  return perevod(int(chislo, base1), base2)

A = input().split()
if int(A[1]) > 36:
  print("Base > 36 !!!")
  exit(-1)
print(perevod_any(A[0].lower(), int(A[1]), int(A[2])))

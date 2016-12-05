def proverka(A):
    if A.count('(') == A.count(')'):
        return True
    else:
        return False


class Smile:
    def __init__(self, str):
        self.str = str
        self.igra(input())

    def __str__(self):
        return self.str

    def additional(self, x):
        if str(x) == ')':
            return self.str+')'
        elif str(x) == '(':
            return self.str+'('
    def igra(self,a):
        while a != 'end':
            if a == '+(':
                self.str = self.additional(a[1:])
                a=input()
            elif a == '+)':
                self.str = self.additional(a[1:])
                a=input()
            elif a == 'print':
                print(self)
                a=input()
            elif a == 'status':
                if proverka(self.str)==True:
                    print('nice')
                    a = input()
                else:
                    print('everything is bad')
                    a = input()
            else:
                print('Vvedi zanovo, mraz:')
                a = input()
    def status(self,str):
        return proverka(self.str)

A = Smile(input())




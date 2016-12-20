class LinkedList:
    def __init__(self):
        self._A=None

    def __str__(self):
        return self._A

    def push_front(self,data):
        p=self._A
        self._A=[data, p]

    def empty(self):
        return not self._A

    def pop_front(self):
        if self.empty():
            raise IndexError()
        data = self._A[1]
        return data

def correct_braces_expressions(s):
    left = ['(','[']; right = [')',']']
    pair = dict(zip(left,right))
    stack = LinkedList()
    for brace in s:
        if brace in left:
            stack.push_front(brace)
        elif brace in right:
            if stack.empty():
                return False
            try:
                if brace != pair[stack.pop_front()]:
                    return False
            except:
                return True
    return stack.empty()

print(correct_braces_expressions('([][])'))

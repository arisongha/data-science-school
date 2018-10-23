# 스택 구현

class Stack :
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container :
            return True
        return False
    
    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]


# 구현 TEST
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

while not s.empty():
    print(s.pop(), end=' ')



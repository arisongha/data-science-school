
# 두 개의 스택을 이용해서 큐를 구현하기

from stack1 import LStack

class SQueue:
    def __init__(self):
        self.first = LStack()
        self.second = LStack()

    def empty(self):
        if self.first.empty() and self.second.empty():
            return True
        return False
    
    # dequeue 와 peek 의 공통 소스 function
    def __shift_stack(self):
        if self.empty():
            return None
        
        # 두번째 스택이 비어있다면
        if self.second.empty():
            # 첫번째 스택이 비어있을 때까지 
            while not self.first.empty():
                # 첫번째 스택에서 pop한 후 그 데이터를 두번째 스택에 push 한다.
                self.second.push(self.first.pop())

    def enqueue(self, data):
        self.first.push(data)

    def dequeue(self):
        # __shift_stack 한 후에 두번째 스택에 쌓여있는 data를 pop한다.
        self.__shift_stack()
        return self.second.pop()

    def peek(self):
        return self.second.peek()


q= SQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

while not q.empty():
    print(q.dequeue(), end= '  ')
print()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

if __name__=="__main__":
    data = [1,2,3,4]
    stack = Stack()
    q = Queue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    flag = True
    while flag == True:
        mid = int(int(stack.size())/2)
        temp = mid
        print(mid)
        while stack.size() > 1:
            q.enqueue(stack.pop())
            temp = temp-1
        print(stack.size())
        print(q.size())
        flag=False

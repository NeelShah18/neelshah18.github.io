"""
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.
Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwords from the end state.
"""

#Queue implementation
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

#class implementation
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
    
    def pr(self):
        return self.stack

#solution
def solution():
    data = [1,2,3,4]
    stack = Stack()
    q = Queue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    flag = True
    y=1
    count = 1
    while count < 4:
        while stack.size() > y:
            temp = stack.pop()
            q.enqueue(temp)
        
        while q.size() >= 1:
            temp2 = q.dequeue()
            stack.push(temp2)
        
        y= y+1
        count = count + 1
    print(stack.pr())
    return None

if __name__=="__main__":
    solution()
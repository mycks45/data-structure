from collections import deque

class Queue:

    def __init__(self):
        self.que = deque()
    
    def enqueque(self, value):
        self.que.appendleft(value)
    
    def dequeque(self):
        return self.que.pop()
    
    
queue = Queue()
queue.enqueque('harshad')
queue.enqueque('sam')
queue.enqueque('anfus')
queue.enqueque('smeeh')

print(queue.dequeque())


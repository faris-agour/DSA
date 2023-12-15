from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
        self.length = 0

    def enqueue(self, value):
        self.length += 1
        return self.queue.appendleft(value)

    def dequeue(self):
        self.length -= 1
        return self.queue.pop()

    def rare(self):
        if self.queue:
            return self.queue[0]
        return None

    def front(self):
        if self.queue:
            return self.queue[-1]
        return None

    def print_queue(self):
        for i in self.queue:
            print(i, end=" ")


q = Queue()
q.enqueue(12)
# q.enqueue(22)
# q.enqueue(1)
# q.enqueue(111)
q.dequeue()
q.print_queue()
print('\n---------')
print(q.rare())
print(q.front())

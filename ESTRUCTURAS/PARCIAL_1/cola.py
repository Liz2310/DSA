#  Implementacion de cola estatica (con arreglos)

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return self.queue == []

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            return True
        return False

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
            return True
        return False

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return False

    def __str__(self):
        return f"Queue: {self.queue}"


if "__name__" == "main":
    q = Queue(7)
    print(q)
    print(q.is_empty())
    print(q.is_full())
    print(q.dequeue())
    print(q.enqueue(0))
    print(q)

    for i in range(1, 7):
        q.enqueue(i)

    print(q)
    print(q.is_full())
    print(q.dequeue())
    print(q)
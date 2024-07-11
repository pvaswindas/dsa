from collections import deque


class QueueUsingDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        item = self.queue.popleft()
        print(f"Dequeued: {item}")
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def display(self):
        print(f"Queue: {list(self.queue)}")


q = QueueUsingDeque()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()
q.front()
q.is_empty()
q.size()

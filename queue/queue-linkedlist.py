class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data


q = LinkedListQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.peek())
print(q.size())
print(q.is_empty())
q.dequeue()
q.dequeue()
print(q.is_empty())

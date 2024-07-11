class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
stack.push('d')
stack.push('e')

print(stack.top.data)

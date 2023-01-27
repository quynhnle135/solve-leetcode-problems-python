class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        return self.items.pop()

    def peek(self):
        return self.items[-1]


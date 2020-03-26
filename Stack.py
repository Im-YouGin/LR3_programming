class Stack:
    def __init__(self):
        self.container = []

    @property
    def empty(self):
        return self.container == []

    def push(self, element):
        self.container.append(element)

    def pop(self):
        return self.container.pop()

    @property
    def top(self):
        return self.container[-1] if not self.empty else None
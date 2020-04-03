class Stack:
    def __init__(self, size):
        self.container = [None] * size
        self.maxsize = size
        self.top_ind = -1

    @property
    def empty(self):
        return self.top_ind == -1

    def push(self, element):
        if self.top_ind == self.maxsize:
            print('Overflow error!')
            exit(0)
        else:
            self.top_ind += 1
            self.container[self.top_ind] = element

    def pop(self):
        if self.top_ind == -1:
            print('Nothing to pop!')
            exit(0)
        else:
            element = self.container[self.top_ind]
            self.top_ind -= 1
        return element

    @property
    def top(self):
        return self.container[self.top_ind] if not self.empty else None

if __name__ == '__main__':
    #Functionality test
    stack = Stack(size=500)
    stack.push(2)
    stack.push(5)
    stack.push(2)
    stack.push(1)
    stack.pop()
    print(stack.top)
    print(stack.container[:5])
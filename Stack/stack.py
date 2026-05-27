class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def get_size(self):
        return len(self.stack)  
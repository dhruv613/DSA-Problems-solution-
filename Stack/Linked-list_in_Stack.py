class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if not self.top:
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def get_size(self):
        return self.size


# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print("stack.peek():", stack.peek())  # Output: 3
print("stack.pop():", stack.pop())   # Output: 3
print("stack.peek():", stack.peek())  # Output: 2
print("stack.get_size():", stack.get_size())  # Output: 2
stack.push(4)
print("stack.peek():", stack.peek())  # Output: 4
print("stack.get_size():", stack.get_size())  # Output: 3
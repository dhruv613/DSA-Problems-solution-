class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Example usage:
queue = Queue()
queue.enqueue(1)    
queue.enqueue(2)
queue.enqueue(3)    
print("queue.dequeue():", queue.dequeue())  # Output: 1
print("queue.size():", queue.size())  # Output: 2
print("queue.is_empty():", queue.is_empty())  # Output: False
print("queue.dequeue():", queue.dequeue())  # Output: 2
print("queue.size():", queue.size())  # Output: 2
print("queue.is_empty():", queue.is_empty())  # Output: False
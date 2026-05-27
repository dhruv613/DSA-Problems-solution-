class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        new_node = Node(item)
        # If the queue is empty, both front and rear will point to the new node
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        # If the queue is not empty, add the new node at the end and update rear
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        # Store the front node and move the front pointer to the next node
        pop_node = self.front
        self.front = self.front.next
        self.size -= 1
        return pop_node.data
    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data  

    def get_size(self):
        return self.size
# Example usage:

if __name__ == "__main__":  
    queue = Queue()
    queue.enqueue(5)    
    queue.enqueue(4)
    queue.enqueue(3)    
    queue.enqueue(1)    

    print("queue.get_front():", queue.get_front())  # Output: 5
    queue.dequeue() # Output: 5
    print("queue.get_front():", queue.get_front())  # Output: 4
    print("queue.get_size():", queue.get_size())  # Output: 3
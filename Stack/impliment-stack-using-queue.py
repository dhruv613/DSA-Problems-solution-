class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []


    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        pop_element = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return pop_element
        

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return not self.queue1
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(4)

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print("param_2:", param_2)  # Output: 2
print("param_3:", param_3)  # Output: 7
print("param_4:", param_4)  # Output: True
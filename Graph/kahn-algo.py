from collections import deque
from typing import List

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = Queue()
        adj_list = []
        indegree = [0] * numCourses
        ans = []

        for i in range(numCourses):
            adj_list.append([])


        for a,b in prerequisites:
            adj_list[a].append(b)
            indegree[b] += 1

        # if the node is independent then add in ans 
        for i in range(numCourses):
            if indegree[i] == 0:
                ans.append(i)
                q.enqueue(i)

        while not q.is_empty():
            front = q.dequeue()
            # remove 1 ffrom from the indegree duering iteration 
            for i in adj_list[front]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    ans.append(i)
                    q.enqueue(i)

        return len(ans) == numCourses

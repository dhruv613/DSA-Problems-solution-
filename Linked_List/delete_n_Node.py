

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(n, edges, s):
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        u, v, w = edge
        adj_list[u-1].append((v-1, w))
        adj_list[v-1].append((u-1, w))

    distances = [float('inf')] * n
    distances[s-1] = 0

    min_heap = [(0, s-1)]
    while len(min_heap) != 0:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in adj_list[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    result = []
    for i, distance in enumerate(distances):
        if i == s - 1:
            continue
        result.append(-1 if distance == float('inf') else distance)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

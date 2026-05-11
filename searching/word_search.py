from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        board_counter = Counter([char for row in board for char in row])
        word_counter = Counter(word)
        for char in word_counter:
            if word_counter[char] > board_counter[char]:
                return False
        visited = [[False for _ in range(n)] for _ in range(m)]
        

# Example usage:
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "SEE"
solution = Solution()
print(solution.exist(board, word))  # Output: True
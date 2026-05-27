class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        self.stack = []

        for char in s:
            if char in ['(', '{', '[']:
                self.stack.append(char)
            else:
                # If the stack is empty, it means there's no opening bracket for the current closing bracket
                if not self.stack:
                    return False
                top = self.stack.pop()
                if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                    return False
        return not self.stack

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "/"
    print("Is the string valid?", solution.isValid(s))  # Output: True

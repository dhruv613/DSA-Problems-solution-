class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def process_string(string):
            st = []
            for char in string:
                if char == '#':
                    if st:
                        st.pop()
                else:
                    st.append(char)
            return st
        return process_string(s) == process_string(t)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "a#c#"
    t = "bc##"
    print("Do the strings are equal?", solution.backspaceCompare(s, t))  # Output: True
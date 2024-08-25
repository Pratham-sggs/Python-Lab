class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        stack = []
        real_longest = 0
        start = -1
        
        for i in range(length):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        real_longest = max(real_longest, i - start)
                    else:
                        real_longest = max(real_longest, i - stack[-1])

        return real_longest

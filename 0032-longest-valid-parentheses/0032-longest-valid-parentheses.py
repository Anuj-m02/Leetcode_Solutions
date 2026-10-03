class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1]
        maxi = 0
        for i in range(n):
            if s[i] == "(" :
                stack.append(i)
            else :
                stack.pop()
                if len(stack) == 0 :
                    stack.append(i)
                else :
                    maxi = max(maxi , i - stack[-1])
        return maxi
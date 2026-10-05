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
    

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxi = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxi = max(maxi, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxi = max(maxi, 2 * left)
            elif left > right:
                left = right = 0
        return maxi
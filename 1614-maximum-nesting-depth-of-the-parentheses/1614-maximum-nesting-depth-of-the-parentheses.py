class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        stack = []
        maxi = -1
        for i in range(n):
            if s[i] == ")" and stack :
                stack.pop()
                maxi = max(len(stack),maxi)
            if s[i] == "(" :
                stack.append(s[i])
        return maxi+1



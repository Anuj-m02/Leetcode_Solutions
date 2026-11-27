class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)

        stack = []

        for i in range(n) :
            curr = s[i]

            stack.append(curr)
            if len(stack) >= 3 and stack[-3 : ] == ["a" , "b" , "c"] :
                stack.pop()
                stack.pop()
                stack.pop()

        return len(stack) == 0 
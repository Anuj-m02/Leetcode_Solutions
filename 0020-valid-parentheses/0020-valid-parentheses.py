class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_parentheses = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_parentheses:
                if stack and stack[-1] == matching_parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack

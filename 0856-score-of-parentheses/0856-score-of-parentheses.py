class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        n = len(s)
        # open_indx , nested_cnt
        stack = [0]
        score = 0

        for indx , char in enumerate(s) :

            if char == "(" :
                stack.append(0)
            
            else :
                v = stack.pop()
                stack[-1] += max(2*v , 1)
        
        return stack.pop()


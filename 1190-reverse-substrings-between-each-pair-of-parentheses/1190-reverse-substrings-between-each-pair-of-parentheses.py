class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        n = len(s)
        pair = [0]*(n)
        stack = []

        # for indx , char in enumerate(s) :
        #     if char == "(" :
        #         stack.append(indx)
        #     elif char == ")" :
        #         j = stack.pop()
        #         pair[indx] = j
        #         pair[j] = indx
        
        for char in s :
            if char == ")" :

                temp = []
                while stack and stack[-1] != "(" :
                    temp.append(stack.pop())
                
                stack.pop()

                stack.extend(temp)
            else :
                stack.append(char)
        
        return "".join(stack)
        
        # res = []
        # curr , direction = 0 , 1

        # while curr < n :
        #     if s[curr] in "()" :
        #         curr = pair[curr]
        #         direction = -direction
            
        #     else :
        #         res.append(s[curr])
            
        #     curr += direction
        
        # return "".join(res)

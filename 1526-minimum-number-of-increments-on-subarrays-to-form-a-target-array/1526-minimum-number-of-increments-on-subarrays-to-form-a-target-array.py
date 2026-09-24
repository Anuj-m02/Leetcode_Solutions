class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        
        n = len(target)
        # res , prev = 0, 0
        # for x in target :
        #     if x > prev :
        #         res += x-prev
            
        #     prev = x
        
        # return res

        stack = []
        op = 0

        for num in target :

            # if curr_ele smaller
            if stack and stack[-1] > num :
                op += stack[-1]-num
                while stack and stack[-1] > num :
                    stack.pop()
            
            # print(stack)
            
            stack.append(num)
        
        if stack :
            op += stack[-1]
        
        return op

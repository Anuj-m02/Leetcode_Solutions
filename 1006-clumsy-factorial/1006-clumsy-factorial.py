# class Solution:
#     def clumsy(self, n: int) -> int:
        
#         stack = [n]
#         cnt = 0
#         curr_num = n-1
#         while stack and curr_num > 0 :
#             if cnt%4 == 0 :
#                 prev = stack.pop()
#                 stack.append(prev*curr_num)
    
#             elif cnt%4 == 1 :
#                 prev = stack.pop()
#                 stack.append(prev//curr_num)
             
#             elif cnt%4 == 2 :
#                 stack.append(curr_num)
    
#             elif cnt%4 == 3 :
#                 stack.append(-curr_num)
            
#             curr_num -= 1
#             cnt  += 1

#         return sum(stack)


class Solution:
    def clumsy(self, n: int) -> int:
        
        stack = [n]
        cnt = 0
        curr_num = n - 1
        
        while curr_num > 0:
            if cnt % 4 == 0:  # Multiplication
                prev = stack.pop()
                stack.append(prev * curr_num)
            elif cnt % 4 == 1:  # Floor Division
                prev = stack.pop()
                stack.append(int(prev / curr_num))  # int() truncates toward zero
            elif cnt % 4 == 2:  # Addition
                stack.append(curr_num)
            elif cnt % 4 == 3:  # Subtraction
                stack.append(-curr_num)
            
            cnt += 1
            curr_num -= 1

        return sum(stack)
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
        
#         # store char and cnt in stack
#         stack = []
#         n = len(s)

#         for i in range(n) :
#             curr_char = s[i]
#             chk = False

#             while stack and stack[-1][0] == curr_char :
#                 if stack[-1][1] == k-1 :
#                     chk = True
#                     stack.pop()
#                     # print(stack)

#                 else :
#                     curr_char , curr_cnt = stack.pop()
#                     chk = True
#                     stack.append((curr_char , curr_cnt+1))
#                     # print(stack)
            
#             if not chk :
#                 stack.append((curr_char , 1))
        
#         ans = ""
#         for char , cnt in stack :
#             ans += char*cnt
#         return ans

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # store char and cnt in stack
        stack = []
        n = len(s)

        for i in range(n):
            curr_char = s[i]
            chk = False  # moved inside loop so it resets for s[i]
            
            if stack and stack[-1][0] == curr_char:
                if stack[-1][1] == k - 1:
                    chk = True
                    stack.pop()
                else:
                    top_char, top_cnt = stack.pop()  # renamed to avoid overwriting curr_char
                    chk = True
                    stack.append((top_char, top_cnt + 1))
            
            if not chk:
                stack.append((curr_char, 1))
        
        ans = ""
        for char, cnt in stack:
            ans += char * cnt  # multiply char by count
            
        return ans
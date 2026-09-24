# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
        
#         # store char and cnt in stack
#         stack = []
#         n = len(s)

#         for i in range(n) :
#             curr_char = s[i]
#             chk = False

#             if stack and stack[-1][0] == curr_char :
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
        stack = []  # stores [char, count]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        # Reconstruct the string from character counts
        ans = []
        for char, count in stack:
            ans.append(char * count)
            
        return "".join(ans)
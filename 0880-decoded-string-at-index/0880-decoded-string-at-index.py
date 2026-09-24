# # class Solution:
# #     def decodeAtIndex(self, s: str, k: int) -> str:
        
# #         n = len(s)
# #         res = ""
# #         stack = []

# #         for i in range(n):
# #             curr = s[i]
# #             while stack and stack[-1] not in "123456789" :
# #                 res += stack.pop()

# #             if stack and stack[-1] in "123456789" :
# #                 res += res*(int(stack.pop())-1) 
            
# #             stack.append(s[i])
        

# #         return res

# class Solution:
#     def decodeAtIndex(self, s: str, k: int) -> str:
        
#         size=0

#         for i in s:
#             if i.isdigit():
#                 size*=int(i)
#             else:
#                 size+=1
                
#         for i in reversed(s):
#             k%=size
#             if k==0 and i.isalpha():
#                 return i
#             if i.isdigit():
#                 size//=int(i)
#             else:
#                 size-=1

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        size = 0

        # Step 1: Push running sizes onto the stack
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
            stack.append(size)

        # Step 2: Traverse in reverse, popping sizes off the stack
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            size = stack.pop()  # Get size up to index i

            k %= size  # Map k into the current string segment

            # If k maps to 0 and current char is a letter, we found it
            if k == 0 and char.isalpha():
                return char

        return ""
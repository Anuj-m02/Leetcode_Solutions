# class Solution:
#     def removeSubstring(self, s: str, k: int) -> str:
        

#         n = len(s)

#         stack = []

#         res = ""

#         pattern = '(' * k + ")" * k
#         k2 = 2*k

#         for char in s :
#             stack.append(char)

#             if len(stack) >= k2 and "".join(stack[-k2:]) == pattern :

#                 del stack[-k2:]
        
#         return "".join(stack)

# class Solution:
#     def removeSubstring(self, s: str, k: int) -> str:
#         stack = []
#         open_count = 0  # Tracks consecutive '(' at the top of stack

#         for char in s:
#             if char == '(':
#                 stack.append('(')
#                 open_count += 1
#             else:
#                 # We encountered ')'
#                 if open_count >= k:
#                     # Check if there are already k - 1 consecutive ')' at the end of stack
#                     # stack[-1] to stack[-(k-1)] must all be ')'
#                     matched = True
#                     for i in range(1, k):
#                         if stack[-i] != ')':
#                             matched = False
#                             break

#                     if matched:
#                         # Pop (k - 1) closing brackets and k opening brackets
#                         for _ in range(k - 1):
#                             stack.pop()
#                         for _ in range(k):
#                             stack.pop()

#                         # Recalculate open_count from the top of the stack
#                         open_count = 0
#                         for idx in range(len(stack) - 1, -1, -1):
#                             if stack[idx] == '(':
#                                 open_count += 1
#                             else:
#                                 break
#                     else:
#                         stack.append(')')
#                         open_count = 0
#                 else:
#                     stack.append(')')
#                     open_count = 0

#         return "".join(stack)

class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # Stack entries are mutable lists: [char, count]
        stack = []

        for ch in s:
            if not stack:
                stack.append([ch, 1])
            elif stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

            # Check if a k-balanced substring "("(" * k + ")"* k) was formed
            if (
                len(stack) >= 2
                and stack[-2][0] == '('
                and stack[-1][0] == ')'
                and stack[-2][1] >= k
                and stack[-1][1] == k
            ):
                # Remove k opening and k closing brackets
                stack[-2][1] -= k
                stack[-1][1] -= k

                # Clean up zero counts
                if stack[-1][1] == 0:
                    stack.pop()
                if stack and stack[-1][1] == 0:
                    stack.pop()

                # Merge adjacent runs of the same character if formed after removal
                if len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                    stack[-2][1] += stack.pop()[1]

        # Reconstruct final string
        return "".join(char * count for char, count in stack)
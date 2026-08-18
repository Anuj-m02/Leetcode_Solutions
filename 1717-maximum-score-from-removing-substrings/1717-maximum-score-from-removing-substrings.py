# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
        
#         n = len(s)
#         # if y > x :

#         total = 0
#         # first remove all ba 
#         stack = []
#         for i in range(n):
#             curr_char = s[i]
#             if stack and stack[-1] == "b" and curr_char == "a":
#                 stack.pop()
#                 total += x
#             else :
#                 stack.append(curr_char)

#         # print(stack)

#         # # now remove all ab
#         rem_stack = []
#         for char in stack :
#             if rem_stack and rem_stack[-1] == "a" and char == "b" :
#                 rem_stack.pop()
#                 total += y
#             else :
#                 rem_stack.append(char)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        total = 0

        # Case 1: x > y -> remove "ab" first, then "ba"
        if x > y:
            # First pass: remove "ab"
            stack = []
            for i in range(n):
                curr_char = s[i]
                if stack and stack[-1] == "a" and curr_char == "b":
                    stack.pop()
                    total += x
                else:
                    stack.append(curr_char)

            # Second pass: remove "ba"
            rem_stack = []
            for char in stack:
                if rem_stack and rem_stack[-1] == "b" and char == "a":
                    rem_stack.pop()
                    total += y
                else:
                    rem_stack.append(char)

        # Case 2: y >= x -> remove "ba" first, then "ab"
        else:
            # First pass: remove "ba"
            stack = []
            for i in range(n):
                curr_char = s[i]
                if stack and stack[-1] == "b" and curr_char == "a":
                    stack.pop()
                    total += y
                else:
                    stack.append(curr_char)

            # Second pass: remove "ab"
            rem_stack = []
            for char in stack:
                if rem_stack and rem_stack[-1] == "a" and char == "b":
                    rem_stack.pop()
                    total += x
                else:
                    rem_stack.append(char)

        return total
# class Solution:
#     def braceExpansionII(self, expression: str) -> list[str]:
        
#         n = len(expression)

#         queue = deque([expression])
#         res = set()

#         while queue :
#             expr = queue.popleft()

#             if "{" not in expr :
#                 res.add(expr) 
#                 continue
            
#             right = expr.find("}")
#             left = expr.find("{" , 0 , right)

#             prefix = expr[:left]
#             suffix = expr[right+1:]

#             inner = expr[left+1:right].split(",")

#             for word in inner :
#                 queue.append(prefix + word + suffix)
        
#         return sorted(list(res))
#         # grps = []
#         # stack = []
#         # curr = [""]

#         # for char in expression :
#         #     if char.isalpha() :

#         #         curr = [s + char for s in curr]
            
#         #     elif char == "{" :
#         #         stack.append((grps , curr))
#         #         grps, curr = [] , [""]
            
#         #     elif char == "," :
#         #         grps.append(curr)
#         #         curr = [""]
            
#         #     elif char == "}" :
#         #         grps.append(curr)

#         #         union_set = set()

#         #         for g in grps :
#         #             union_set.update(g)
                
#         #         prev_grps , prev_curr = stack.pop()
#         #         curr = [p + u for p in prev_curr for u in union_set]
#         #         grps = prev_grps
            
#         # grps.append(curr)
#         # res = set()
#         # for g in grps :
#         #     res.update(g)
        
#         # return sorted(list(res))


from collections import deque

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        queue = deque([expression])
        res = set()

        while queue:
            # print(queue)
            expr = queue.popleft()
            # print(expr)

            # If no braces left, we have a fully formed word
            if '{' not in expr:
                res.add(expr)
                continue

            # Find the first closing brace '}'
            right = expr.find('}')
            # Find the matching opening brace '{' right before it
            left = expr.rfind('{', 0, right)

            # Extract the prefix, inner sub-expression, and suffix
            prefix = expr[:left]
            suffix = expr[right + 1:]
            inner = expr[left + 1:right].split(',')

            # Generate new expressions by replacing the brace group
            for word in inner:
                queue.append(prefix + word + suffix)

        return sorted(list(res))
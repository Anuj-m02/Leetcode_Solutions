from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        found = False
        res = []

        while queue:
            curr = queue.popleft()
            
            if is_valid(curr):
                res.append(curr)
                found = True  # Stop generating further levels once a valid level is reached
            
            if found:
                continue

            # Try removing each parenthesis one by one
            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return res


# class Solution:
#     def removeInvalidParentheses(self, s: str) -> list[str]:
        
#         n = len(s)

#         def valid(removed) :
#             indx = 0
#             cnt_open , cnt_close = 0 , 0
#             while indx < n :
#                 if s[indx] not in removed :
#                     if s[indx] == "(" :
#                         cnt_open += 1
#                     else :
#                         cnt_close += 1
                
#                 if cnt_close > cnt_open :
#                     return False
            
#             return cnt_open == cnt_close 

#         min_removals = float("inf")
#         valid_strings = set()

#         @lru_cache(maxsize=None)
#         def dp(indx , removed) :
#             nonlocal min_removals

#             if len(removed) > min_removals :
#                 return 
            
#             if indx >= n :
#                 if valid(removed) :
#                     rem_cnt = len(removed)
#                     curr_str = "".join(s[i] for i in range(n) if i not in removed)

#                     if rem_cnt < min_removals :
#                         min_removals = rem_cnt
#                         valid_strings.clear()
#                         valid_strings.add(curr_str)
#                     elif rem_cnt == min_removals :
#                         valid_strings.add(curr_str)
                
#                 return
            
#             if s[indx] in "()" :
#                 # not_take
#                 not_take = dp(indx+1 , removed | frozenset({indx}))
#                 take = dp(indx+1 , removed)
            
#             else :
#                 # char
#                 dp(indx+1 , removed)


#         dp(0 , frozenset()) 
#         return list(valid_strings)

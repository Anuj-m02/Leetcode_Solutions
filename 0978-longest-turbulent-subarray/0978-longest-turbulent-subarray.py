# # class Solution:
# #     def maxTurbulenceSize(self, arr: List[int]) -> int:

# #         n = len(arr)

# #         @cache
# #         def dp(indx , prev_sign) :

# #             if indx == n-1 :
# #                 return 0
            
# #             curr_ele ,nxt_ele = arr[indx] , arr[indx+1]
# #             op1 , op2 = float('-inf') , float("-inf")

# #             if prev_sign == -1 :
# #                 # this means we are starting from here
# #                 if nxt_ele > curr_ele :
# #                     op1 = 1 + dp(indx+1 , 1)
# #                 else :
# #                     op2 = 1 + dp(indx+1 , 0)

# #             if prev_sign == 0 :
# #                 # prev was less now next must be greter than curr
# #                 if nxt_ele > curr_ele :
# #                     op1 =  1+dp(indx+1 , 1-prev_sign)
                
# #                 else :
# #                     # now start from this new_indx 
# #                     op2 = dp(indx+1 , -1)
            
# #             else :
# #                 if nxt_ele < curr_ele :
# #                     op1 = 1 + dp(indx+1 , 1-prev_sign)
                
# #                 else :
# #                     op2 = dp(indx+1 , -1)
            
# #             return max(op1 , op2)
        
# #         return dp(0,-1)
# from functools import lru_cache
# import sys

# # Increase recursion depth to handle max constraints (n = 40,000)
# sys.setrecursionlimit(10**6)

# class Solution:
#     def maxTurbulenceSize(self, arr: list[int]) -> int:
#         n = len(arr)
#         if n == 1:
#             return 1

#         @lru_cache(None)
#         def dp(indx, prev_sign):
#             if indx == n - 1:
#                 return 1  # Base case: a single element array has length 1

#             curr_ele, nxt_ele = arr[indx], arr[indx + 1]

#             # 1. Starting fresh from indx
#             if prev_sign == -1:
#                 if nxt_ele > curr_ele:
#                     return max(1 + dp(indx + 1, 1), dp(indx + 1, -1))
#                 elif nxt_ele < curr_ele:
#                     return max(1 + dp(indx + 1, 0), dp(indx + 1, -1))
#                 else:
#                     return dp(indx + 1, -1)

#             # 2. Previous comparison was '<' (prev_sign == 0), now need '>'
#             elif prev_sign == 0:
#                 if nxt_ele > curr_ele:
#                     return 1 + dp(indx + 1, 1)
#                 else:
#                     # Sign failed to alternate; check starting fresh at indx or indx+1
#                     return dp(indx, -1)

#             # 3. Previous comparison was '>' (prev_sign == 1), now need '<'
#             else:
#                 if nxt_ele < curr_ele:
#                     return 1 + dp(indx + 1, 0)
#                 else:
#                     # Sign failed to alternate; check starting fresh at indx or indx+1
#                     return dp(indx, -1)

#         return dp(0, -1)

from functools import cache

class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        @cache
        def dp(indx, prev_sign):
            """
            Returns the max length of a turbulent subarray 
            STARTING at `indx` given the `prev_sign`.
            
            prev_sign:
             -1 : First element of a new turbulent sequence
              0 : Previous comparison was '<' (need next to be '>')
              1 : Previous comparison was '>' (need next to be '<')
            """
            if indx == n - 1:
                return 1

            curr_ele, nxt_ele = arr[indx], arr[indx + 1]

            # Case 1: Fresh start at indx
            if prev_sign == -1:
                if nxt_ele > curr_ele:
                    return 1 + dp(indx + 1, 0)
                elif nxt_ele < curr_ele:
                    return 1 + dp(indx + 1, 1)
                else:
                    return 1

            # Case 2: Previous comparison was '<', need '>'
            elif prev_sign == 0:
                if curr_ele > nxt_ele:
                    return 1 + dp(indx + 1, 1)
                else:
                    return 1  # Cannot extend further

            # Case 3: Previous comparison was '>', need '<'
            else:
                if curr_ele < nxt_ele:
                    return 1 + dp(indx + 1, 0)
                else:
                    return 1  # Cannot extend further

        # Test starting a fresh turbulent sequence from EVERY possible index
        return max(dp(i, -1) for i in range(n))
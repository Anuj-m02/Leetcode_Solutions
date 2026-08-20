# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:

#         n = len(arr)
#         visited = set()        

#         # @lru_cache(maxsize=None)
#         def dp(indx) :

#             if arr[indx] == 0 :
#                 return True
            
#             if indx in visited :
#                 return False
            
#             visited.add(indx)
            
#             ans = False
#             op1 , op2 = min(indx + arr[indx] , n-1) , max(indx - arr[indx] , 0)
#             # visited.add(op1)
#             # visited.add(op2)

#             if dp(op1) or dp(op2) :
#                 return True
            
#             return False
        
#         return dp(start)

from collections import defaultdict, deque, Counter
import heapq
from functools import lru_cache
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)        
        visited = set()

        def dp(indx):
            # Base cases: out of bounds or loop detected
            if indx < 0 or indx >= n or indx in visited:
                return False

            if arr[indx] == 0:
                return True
            
            visited.add(indx)
            
            op1 = indx + arr[indx]
            op2 = indx - arr[indx]

            if dp(op1) or dp(op2):
                return True
            
            return False
        
        return dp(start)
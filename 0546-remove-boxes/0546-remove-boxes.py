from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        n = len(boxes)

        # at each indx we have option either to continue streak if streak is running
        # else start new streak

        # @lru_cache(maxsize=None)
        # def dp(indx , prev_val , curr_streak_len) :

        #     if indx == n :
        #         return curr_streak_len**2
            
        #     curr_val = boxes[indx]
        #     temp1 , temp2 = float('-inf') , float("-inf")
        #     if curr_val == prev_val :
        #         temp1 = dp(indx+1 , curr_val , curr_streak_len+1)
            
        #     # new_streak
        #     temp2 = (curr_streak_len**2) + dp(indx+1 , curr_val , 1)

        #     return max(temp1 , temp2)

        @lru_cache(maxsize=None)
        def dp(left , right , k) :

            if left > right :
                return 0
            
            while left < right and boxes[left] == boxes[left+1] :
                left += 1
                k += 1
            

            res = (k+1)**2 + dp(left+1 , right , 0)

            for m in range(left+1  , right+1) :
                if boxes[m] == boxes[left] :
                    res = max(res , dp(left+1 , m-1 , 0 ) + dp(m , right , k+1))
            
            return res
        

        return dp(0 , n-1 , 0)

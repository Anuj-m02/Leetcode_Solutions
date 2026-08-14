from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        # next greter element
        # next smaller elemnt
        n = len(arr)

        def make_jumps(sorted_indices) :
            next_jump = [-1]*(n)
            stack = []
            for indx in sorted_indices :
                while stack and stack[-1] < indx :
                    next_jump[stack.pop()] = indx
                stack.append(indx)
            
            return next_jump
        
        sorted_indices = sorted(range(n) , key = lambda indx : (arr[indx] , indx))
        next_odd = make_jumps(sorted_indices)

        sorted_indices = sorted(range(n) , key = lambda indx : (-arr[indx] , indx))
        next_even = make_jumps(sorted_indices)

        n = len(arr)

        @lru_cache(maxsize=None)
        def dp(indx , jump) :

            if indx == n-1 :
                return 1
            
            # at each index we have either odd jump or even jump
            # odd jump
            if jump :
                new_indx = next_odd[indx]
                if new_indx != -1 :
                # go to next smallest possible greater value
                    return dp(new_indx , 1-jump)
            
            else :
                new_indx = next_even[indx]
                if new_indx != -1 :
                # go to next largest possible smaller value
                    return dp(new_indx , 1-jump)
            
            return 0
        

        cnt = 0
        for indx in range(n):
            cnt += dp(indx , 1)
        
        return cnt


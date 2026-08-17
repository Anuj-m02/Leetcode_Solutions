from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        n = len(piles)

        @lru_cache(maxsize=None)
        def dp(left , right) :
            if left == right :
                return 0
            
            # pick left
            op1 = piles[left] + dp(left+1 , right )

            #pick right
            op2 = piles[right] + dp(left , right-1)

            return max(op1 , op2)
        
        alice = dp(0 , n-1)
        bob = sum(piles) - alice
        if alice > bob :
            return True
        
        return False
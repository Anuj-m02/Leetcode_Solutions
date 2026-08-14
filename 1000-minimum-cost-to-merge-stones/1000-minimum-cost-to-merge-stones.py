from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)

        if (n-1)%(k-1) != 0 :
            return -1
        
        prefix = [0]*(n+1)
        for i in range(n) :
            prefix[i+1] = prefix[i] + stones[i]

        @lru_cache(maxsize=None)
        def dp(left , right):

            if left == right :
                return 0
            res = float("inf")
            for mid in range(left , right , k-1) :
                res = min(res , dp(left , mid) + dp(mid+1 , right))
            
            if (right-left)%(k-1) == 0 :
                res += prefix[right+1] - prefix[left]
            
            return res
        
        return dp(0,n-1)

            

        

from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        
        n , m = len(grid) , len(grid[0])

        @lru_cache(maxsize=None)
        def dp( j , val) :

            if j == m :
                return 0
            
            cnt = 0
            for i in range(n):
                if grid[i][j] != val :
                    cnt += 1
            
            ans = float("inf")

            for k in range(10) :
                if k == val :
                    continue
                ans = min(ans , cnt + dp(j+1 , k))
            
            return ans
        
        mini = float("inf")
        for i in range(10) :
            mini = min(mini , dp(0,i))
        
        return mini



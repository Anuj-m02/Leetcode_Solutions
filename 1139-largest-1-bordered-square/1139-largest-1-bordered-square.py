from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        n , m = len(grid) , len(grid[0])

        @lru_cache(maxsize=None)
        def get_right(row , col) :
            if row >= n or col >= m or grid[row][col] == 0 :
                return 0
            
            return 1 + get_right(row , col+1)
        
        
        @lru_cache(maxsize=None)
        def get_down(row , col) :
            if row >= n or col >= m or grid[row][col] == 0 :
                return 0
            return 1 + get_down(row+1 , col)
        
        max_side = 0

        for row in range(n):
            for col in range(m) :

                max_poss = min(get_right(row , col) , get_down(row, col))

                for side in range(max_poss , max_side , -1) :

                    if get_right(row+side-1 , col)  >= side and get_down(row , col + side-1) >= side :
                        max_side = side
                        break
        
        return max_side**2
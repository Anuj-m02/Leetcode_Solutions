from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        
        n , m = len(grid) , len(grid[0])
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]

        curr_cost , curr_row , curr_col , curr_turns , prev_dir = grid[0][0] , 0 , 0 , 0 , -1



        heap = [(curr_cost , curr_row , curr_col , curr_turns , prev_dir )]
        dist = defaultdict(lambda : float("inf"))

        dist[(0 , 0 ,0 , -1)] = grid[0][0]

        while heap :
            curr_cost , curr_row , curr_col , curr_turns , prev_dir = heapq.heappop(heap)

            if curr_row == n-1 and curr_col == m-1 :
                return curr_cost

            if dist[(curr_row , curr_col , curr_turns , prev_dir)] < curr_cost :
                continue
            
            for indx , (dx , dy) in enumerate(dirs) :
                new_row , new_col = curr_row + dx , curr_col + dy
                if 0 <= new_row < n and 0 <= new_col < m :

                    new_turns = curr_turns + (1 if prev_dir != -1 and indx != prev_dir else 0)

                    if new_turns <= k :
                        new_cost = grid[new_row][new_col] + curr_cost

                        if dist[(new_row , new_col , new_turns , indx)] > new_cost :
                            dist[(new_row , new_col , new_turns , indx)] = new_cost
                            heapq.heappush(heap , (new_cost , new_row , new_col , new_turns , indx))
            
        return -1




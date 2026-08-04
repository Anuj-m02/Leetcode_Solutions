from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        # Check if we are trapped at the origin
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dist = [[float("inf")]*m for _ in range(n)]

        dist[0][0] = 0

        dirs = [(-1,0) , (1,0) , (0,1) , (0,-1)]

        heap = [(0,0,0)]
        # curr_time , curr_row , curr_col

        while heap :
            curr_time , curr_row , curr_col = heapq.heappop(heap)

            if curr_row == n-1 and curr_col == m-1 :
                return curr_time

            if dist[curr_row][curr_col] < curr_time :
                continue
            
            for dr , dc in dirs :
                new_row , new_col = curr_row + dr , curr_col + dc
                new_time = curr_time + 1

                if 0 <= new_row < n and 0 <= new_col < m :
                    if grid[new_row][new_col] <= curr_time + 1 :
                        new_time = curr_time+1
                    else :
                        diff = grid[new_row][new_col] - curr_time
                        if diff%2 :
                            new_time = grid[new_row][new_col]
                        else :
                            new_time = grid[new_row][new_col] + 1
                    
                    if new_time < dist[new_row][new_col] :
                        dist[new_row][new_col] = new_time
                        heapq.heappush(heap , (new_time , new_row , new_col))
        

        return -1
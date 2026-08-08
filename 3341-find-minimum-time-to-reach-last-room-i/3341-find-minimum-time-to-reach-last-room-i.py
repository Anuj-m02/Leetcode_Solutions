from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        n , m = len(moveTime) , len(moveTime[0])

        dirs = [(0,1) , (1,0) , (0,-1) , (-1,0)]

        # start from 0,0
        # curr_time , curr_row , curr_col
        heap = [(0 , 0 , 0)]
        dist = [[float("inf")]*m for _ in range(n)]

        while heap :

            curr_time , curr_row , curr_col = heapq.heappop(heap)

            if dist[curr_row][curr_col] < curr_time :
                continue
            
            for dr , dc in dirs :
                new_row , new_col = curr_row + dr , curr_col+dc
                if 0 <= new_row < n and 0 <= new_col < m :
                    wait_time , new_time = 0 ,0 
                    if moveTime[new_row][new_col] > curr_time :
                        wait_time = moveTime[new_row][new_col] - curr_time
                        new_time = curr_time + wait_time + 1
                    else :
                        wait_time = 0
                        new_time = curr_time + 1

                    if dist[new_row][new_col] > new_time :
                        dist[new_row][new_col] = new_time
                        heapq.heappush(heap , (new_time , new_row , new_col))

        
        return dist[n-1][m-1]

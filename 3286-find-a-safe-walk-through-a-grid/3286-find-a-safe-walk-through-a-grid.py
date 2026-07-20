from functools import lru_cache
from collections import defaultdict , deque
import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        n , m = len(grid) , len(grid[0])
        dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]
        best = [[-1]*m for _ in range(n)]

        if grid[0][0] == 1 :
            health -= 1
        if health < 1 :
            return False

        best[0][0] = health

        queue = deque([(0,0,health)])

        while queue :
            curr_row , curr_col , curr_health = queue.popleft()

            if curr_health < 1 :
                continue

            if curr_row == n-1 and curr_col == m-1 and curr_health >= 1 :
                return True
            
            for dx , dy in dirs :
                new_row , new_col = curr_row+dx , curr_col + dy
                if 0 <= new_row < n and 0 <= new_col < m :

                    new_health = curr_health - grid[new_row][new_col]
                    if new_health < 1 :
                        continue
                    
                    if new_health > best[new_row][new_col] :
                        best[new_row][new_col] = new_health
                        queue.append((new_row , new_col , new_health))

        return False




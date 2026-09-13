# from functools import lru_cache
# import heapq
# from collections import defaultdict , deque , Counter


# class Solution:
#     def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:


#         heap = []
#         dist = [[float("inf")]*n for _ in range(m)]
#         dist[0][0] = 1
#         start_row , start_col , start_cost , start_action = 0 , 0 , 1 , 1

#         heapq.heappush(heap , (start_cost , start_row , start_col , start_action))

#         while heap :
#             curr_cost , curr_row , curr_col , curr_action = heapq.heappop(heap)

#             if curr_row == m-1 and curr_col == n-1 :
#                 return curr_cost
            
#             # odd parity
#             if curr_action % 2 :
#                 new_row , new_col = curr_row , curr_col + 1
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1)
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action))
            
#                 new_row , new_col = curr_row + 1 , curr_col
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1)
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action)) 

#                 new_row , new_col = curr_row , curr_col - 1
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1) + penalty[curr_row][curr_col]
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1 - curr_action))
            
#                 new_row , new_col = curr_row - 1 , curr_col
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1) + penalty[curr_row][curr_col]
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action)) 


#             # even parity
#             if curr_action % 2 == 0 :
#                 new_row , new_col = curr_row , curr_col - 1
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1)
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action))
            
#                 new_row , new_col = curr_row - 1 , curr_col
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1)
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action)) 
            
#                 new_row , new_col = curr_row , curr_col + 1
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1) + penalty[curr_row][curr_col]
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action))
            
#                 new_row , new_col = curr_row + 1 , curr_col
#                 if 0 <= new_row < m and 0 <= new_col < n :
#                     new_dist = curr_cost + (new_row+1)*(new_col+1) + penalty[curr_row][curr_col]
#                     if dist[new_row][new_col] < new_dist :
#                         dist[new_row][new_col] = new_dist
#                         heapq.heappush(heap , (new_dist , new_row , new_col , 1-curr_action)) 

import heapq
from typing import List

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        # State: dist[r][c][parity] where parity = 0 (even) or 1 (odd)
        dist = [[[float("inf")] * 2 for _ in range(n)] for _ in range(m)]
        
        heap = []
        start_row, start_col, start_cost, start_action = 0, 0, 1, 1
        
        # Initial state at (0, 0) before action 1 starts (odd action rule next)
        dist[0][0][1] = start_cost
        heapq.heappush(heap, (start_cost, start_row, start_col, start_action))

        directions = [
            (0, 1, "R"),   # Right
            (1, 0, "D"),   # Down
            (0, -1, "L"),  # Left
            (-1, 0, "U")   # Up
        ]

        while heap:
            curr_cost, curr_row, curr_col, curr_action = heapq.heappop(heap)
            curr_parity = curr_action % 2

            if curr_cost > dist[curr_row][curr_col][curr_parity]:
                continue

            if curr_row == m - 1 and curr_col == n - 1:
                return curr_cost

            next_action = curr_action + 1
            next_parity = next_action % 2

            # Option 1: Move to an adjacent cell
            for dr, dc, move_dir in directions:
                new_row, new_col = curr_row + dr, curr_col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    # Check if move follows parity rule
                    if curr_parity == 1:  # Odd action: Right or Down
                        is_valid_parity = move_dir in ("R", "D")
                    else:                  # Even action: Left or Up
                        is_valid_parity = move_dir in ("L", "U")

                    cost_add = (new_row + 1) * (new_col + 1)
                    if not is_valid_parity:
                        cost_add += penalty[curr_row][curr_col]

                    new_dist = curr_cost + cost_add
                    if new_dist < dist[new_row][new_col][next_parity]:
                        dist[new_row][new_col][next_parity] = new_dist
                        heapq.heappush(heap, (new_dist, new_row, new_col, next_action))

            # Option 2: Wait in current cell
            wait_cost = curr_cost + penalty[curr_row][curr_col]
            if wait_cost < dist[curr_row][curr_col][next_parity]:
                dist[curr_row][curr_col][next_parity] = wait_cost
                heapq.heappush(heap, (wait_cost, curr_row, curr_col, next_action))

        return -1
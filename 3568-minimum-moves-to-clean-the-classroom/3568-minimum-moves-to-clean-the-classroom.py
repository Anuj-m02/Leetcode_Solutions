# class Solution:
#     def minMoves(self, classroom: List[str], energy: int) -> int:
        
#         n , m = len(classroom) , len(classroom[0])

#         start_row , start_col = 0 , 0
#         cnt = 0
#         for i in range(n):
#             for j in range(m) :
#                 if classroom[i][j] == "S" :
#                     start_row , start_col = i , j
#                 if classroom[i][j] == "L" :
#                     cnt += 1
        
#         dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]
        

#         queue = deque([(start_row , start_col , energy , 0 , 0)])
#         ans = float("inf")

#         while queue :
#             curr_row , curr_col , curr_energy , curr_step , curr_cnt = queue.popleft()

#             if curr_cnt == cnt :
#                 ans = min(ans , curr_step)
            
#             for dx , dy in dirs :
#                 new_row , new_col = curr_row + dx , curr_col + dy
#                 if 0 <= new_row < n and 0 <= new_col < m :
#                     if curr_energy > 0 :

#                         if classroom[new_row][new_col] == "L" :
#                             queue.append((new_row , new_col , curr_energy - 1 , curr_step + 1 , curr_cnt + 1 ))
#                             classroom[new_row][new_col] == "."
                        
#                         elif classroom[new_row][new_col] == "X" :
#                             continue
                        
#                         elif classroom[new_row][new_col] == "R" :
#                             queue.append((new_row , new_col , energy , curr_step + 1 , curr_cnt))
                        
#                         elif classroom[new_row][new_col] == "." :
#                             queue.append((new_row , new_col , curr_energy - 1 , curr_step + 1 , curr_cnt))
        
#         return ans




            



from collections import deque
from typing import List


class Solution:

  def minMoves(self, classroom: List[str], energy: int) -> int:
    n, m = len(classroom), len(classroom[0])

    start_row, start_col = 0, 0
    all_litters = set()

    # Locate starting position 'S' and all litter positions 'L'
    for i in range(n):
      for j in range(m):
        if classroom[i][j] == "S":
          start_row, start_col = i, j
        elif classroom[i][j] == "L":
          all_litters.add((i, j))

    total_litters = len(all_litters)

    # Queue stores: (row, col, collected_frozenset, remaining_energy, steps)
    queue = deque([(start_row, start_col, frozenset(), energy, 0)])

    # Visited state maps (row, col, collected_frozenset) -> max_remaining_energy
    visited = {(start_row, start_col, frozenset()): energy}

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
      r, c, collected, e, steps = queue.popleft()

      # Goal check: all litter items collected
      if len(collected) == total_litters:
        return steps

      # Cannot move further if out of energy
      if e == 0:
        continue

      for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < m:
          cell = classroom[nr][nc]
          if cell == "X":
            continue

          next_collected = collected
          next_energy = e - 1

          if cell == "R":
            next_energy = energy
          elif cell == "L" and (nr, nc) not in collected:
            next_collected = collected | frozenset([(nr, nc)])

          state = (nr, nc, next_collected)

          # Only proceed if we reach this state with strictly more remaining energy
          if visited.get(state, -1) < next_energy:
            visited[state] = next_energy
            queue.append((nr, nc, next_collected, next_energy, steps + 1))

    return -1
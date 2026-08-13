from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache
import bisect


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        

        n = len(robots)
        m = len(walls) 

        walls.sort()
        robot_pairs = sorted(zip(robots , distance))
        # walls in [left , right]
        def count_walls(left , right) :
            if left > right :
                return 0
            left_indx = bisect.bisect_left(walls , left)
            right_indx = bisect.bisect_right(walls , right)
            return right_indx-left_indx

        @lru_cache(maxsize=None)
        def dp(indx , nxt_direction) :

            # 0 robo indx shoot left
            # 1 robo indx shoot right

            if indx < 0 :
                return 0

            pos , dist = robot_pairs[indx]

            # option1 curr_robot shoots left

            left = pos - dist

            if indx > 0 :
                prev_pos , prev_dist = robot_pairs[indx-1]
                left = max(left , prev_pos+1)
            
            #walls in [left , pos]
            
            hits_left = count_walls(left , pos)

            option_left = dp(indx-1 , 0) + hits_left

            # option2 shoots right

            right = pos + dist

            if indx + 1 < n :
                nxt_pos , nxt_dist = robot_pairs[indx+1]

                if nxt_direction == 0 :

                    # nxt robo shoots left
                    right = min(right , nxt_pos - nxt_dist -1 )
                
                else :

                    # nxt robo shoots right

                    right = min(right , nxt_pos-1)
            
            hits_right = count_walls(pos , right)

            option_right = dp(indx-1 , 1) + hits_right

            return max(option_left , option_right)
        
        return dp(n-1 , 1)























        
#         # in dp indx of robots and prev robots pos

#         @lru_cache(maxsize=None)
#         def dp(indx , prev) :
            
#             if indx == n :
#                 return 0
            
#             pos , dist = robo_pairs[indx]

#             left_reach = max(prev + 1  pos-dist)
#             walls_if_left = count_walls(left_reach , pos) + dp(indx+1 , pos)

#             rigth_reach = pos+dist
#             walls_if_right = count_walls(max(prev + 1 , pos) , right_reach) + dp(indx+1 , right_reach)




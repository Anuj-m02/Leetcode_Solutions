# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache
# import bisect


# class Solution:
#     def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        

#         n = len(robots)
#         m = len(walls) 

#         walls.sort()
#         robo_pairs = sorted(zip(robots , distance))

#         # walls in [left , right]
#         def count_walls(left , right) :
#             if left > right :
#                 return 0
#             left_indx = bisect.bisect_left(walls , left)
#             right_indx = bisect.bisect_right(walls , right)
#             return right_indx-left_indx
        
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


from bisect import bisect_left
from functools import lru_cache
from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:

        # Sort robots according to position
        robot_pairs = sorted(zip(robots, distance))
        walls.sort()

        n = len(robot_pairs)

        @lru_cache(None)
        def dp(indx, next_direction):
            """
            next_direction:
                0 -> robot indx is going to shoot LEFT
                1 -> robot indx is going to shoot RIGHT

            dp(indx, next_direction) =
                maximum walls destroyed by robots [0 ... indx]
                assuming robot indx shoots in next_direction.
            """

            if indx < 0:
                return 0

            pos, dist = robot_pairs[indx]

            # --------------------------------------------------
            # Option 1: Current robot shoots LEFT
            # --------------------------------------------------

            left = pos - dist

            # Cannot cross the previous robot
            if indx > 0:
                prev_pos, _ = robot_pairs[indx - 1]
                left = max(left, prev_pos + 1)

            # Walls in [left, pos]
            l = bisect_left(walls, left)
            r = bisect_left(walls, pos + 1)

            hits_left = r - l

            option_left = dp(indx - 1, 0) + hits_left

            # --------------------------------------------------
            # Option 2: Current robot shoots RIGHT
            # --------------------------------------------------

            right = pos + dist

            if indx + 1 < n:
                next_pos, next_dist = robot_pairs[indx + 1]

                if next_direction == 0:
                    # Next robot shoots LEFT.
                    #
                    # Current robot cannot destroy walls
                    # which will also be destroyed by next robot.
                    right = min(
                        right,
                        next_pos - next_dist - 1
                    )
                else:
                    # Next robot shoots RIGHT.
                    #
                    # Current robot cannot cross next robot.
                    right = min(
                        right,
                        next_pos - 1
                    )

            # Walls in [pos, right]
            l = bisect_left(walls, pos)
            r = bisect_left(walls, right + 1)

            hits_right = r - l

            option_right = dp(indx - 1, 1) + hits_right

            return max(option_left, option_right)

        return dp(n - 1, 1)
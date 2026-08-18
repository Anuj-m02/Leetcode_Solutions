from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        n = len(positions)

        arr = []

        for indx , (position , health , direction) in enumerate(zip (positions, healths , directions)) :
            arr.append((position , health , direction , indx))
        
        arr.sort()
        stack = []

        for i in range(n) :
            curr_pos , curr_health , curr_dir , curr_indx = arr[i]
            # stack.append(arr[i]) 
            while stack and stack[-1][2] == "R"  and curr_dir == "L" :
                # collision will happen

                last_pos , last_health , last_dir , last_indx = stack[-1]

                if curr_health > stack[-1][1] :
                    stack.pop()
                    curr_health -= 1
                    # stack.append((arr[i][0] , curr_health-1 , curr_dir , indx ))
                
                elif curr_health == stack[-1][1] :
                    stack.pop()
                    curr_health = 0
                    break
                
                else :
                    stack[-1] = (last_pos , last_health-1 , last_dir , last_indx)
                    curr_health = 0
                    break
                    # stack.append((a , b-1 , c , d ))
            
            if curr_health > 0 :
                stack.append((curr_pos , curr_health , curr_dir , curr_indx))
        

        # sort by indx
        stack.sort(key = lambda x : x[3])
        res = []
        for a , b , c , d in stack:
            res.append(b)
        
        return res


from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        n = len(chargeTimes)

        prefix = [0]*(n+1)
        for i in range(n) :
            prefix[i+1] = prefix[i] + runningCosts[i]

        
        def check(mid) :

            if mid == 0 :
                return True
            
            # -val , indx
            heap = []

            for i in range(n) :
                heapq.heappush(heap , (-chargeTimes[i] , i))

                start_indx = i - mid + 1
                while heap and heap[0][1] < start_indx :
                    heapq.heappop(heap)
                
                if i >= mid-1 :
                    maxi = -heap[0][0]
                    total = prefix[i+1] - prefix[start_indx]

                    if maxi + (mid*total) <= budget :
                        return True
            
            return False


        
        # def check(mid) :

        #     if mid == 0 :
        #         return True

        #     indx = 0
        #     cost = 0
        #     # print(mid)
        #     while indx + mid <= n :
        #         curr_subarr = chargeTimes[indx:indx+mid]
        #         # print(curr_subarr)
        #         maxi = max(curr_subarr)
        #         # print(maxi)
        #         total = prefix[indx+mid] - prefix[indx]
        #         # print(total)
        #         cost =  maxi + (mid * total)
        #         # print(res)
        #         indx += 1

        #         if cost <= budget :
        #             return True
            
        #     # if res <= budget :
        #     #     return True
            
        #     return False



        ans = 0
        low , high = 1 , n
        while low <= high :
            mid = (low+high)//2
            if check(mid) :
                ans = mid
                low = mid + 1
            else :
                high = mid-1
        
        return ans
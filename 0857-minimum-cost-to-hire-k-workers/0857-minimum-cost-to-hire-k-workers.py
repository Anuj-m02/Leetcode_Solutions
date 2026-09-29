# class Solution:
#     def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        
#         n = len(quality)

#         heap = []

#         rate_val , rate_indx = float("inf") , -1
#         for indx in range(n) :
#             temp = wage[indx]/quality[indx]
#             if temp < rate_val :
#                 rate_val , rate_indx = temp , indx

#         # visited = [False]*(n)
#         # visited[rate_indx] = Tr
#         # for indx in range(n) :
#             # curr_amount , curr_no_of_people , rate wage/quality , worker_alrdy_used

#         heapq.heappush(heap , (wage[rate_indx] , 1 , rate_val , frozenset({rate_indx})))
        
#         while heap :
#             curr_amount , curr_people , curr_rate , used_worker = heapq.heappop(heap)
#             if curr_people == k :
#                 return curr_amount
            
#             for indx in range(n) :
#                 if indx not in used_worker :
#                     new_amount , new_people = quality[indx]*curr_rate , curr_people + 1
#                     if new_amount >= wage[indx] :
#                         heapq.heappush(heap , (new_amount + curr_amount , new_people , curr_rate , used_worker | frozenset({indx})))
 
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        n = len(quality)
        
        # 1. Pair workers and sort them by wage/quality ratio ascending
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        
        # 2. Track the smallest qualities using a Max-Heap
        heap = []
        curr_quality_sum = 0
        min_cost = float("inf")
        
        for curr_rate, q in workers:
            # Add current worker's quality (negated for max-heap in Python)
            heapq.heappush(heap, -q)
            curr_quality_sum += q
            
            # If group exceeds size k, pop the worker with the largest quality
            if len(heap) > k:
                curr_quality_sum += heapq.heappop(heap)
            
            # When we have exactly k workers, evaluate total cost
            if len(heap) == k:
                min_cost = min(min_cost, curr_quality_sum * curr_rate)
                
        return min_cost
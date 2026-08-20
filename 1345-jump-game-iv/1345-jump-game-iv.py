from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)

        nxt_equal_indx = [-1]*(n)
        s = set(arr)
        val_to_indx = defaultdict(list)
        for i in range(n) :
            val = arr[i]
            val_to_indx[val].append(i)
        

        queue = deque([(0 , 0)])
        dist = [float("inf")]*(n)

        dist[0] = 0

        while queue :
            curr_node , curr_dis = queue.popleft()
            if curr_node == n-1 :
                return curr_dis
            
            if dist[curr_node] < curr_dis :
                continue

            all_indxs = val_to_indx[arr[curr_node]]

            all_indxs += [curr_node+1 , curr_node-1]
            val_to_indx[arr[curr_node]] = []

            for neighbour in all_indxs :
                if neighbour < n and neighbour >= 0  and neighbour != curr_node :
                    if dist[neighbour] > curr_dis + 1 :
                        dist[neighbour] = curr_dis + 1
                        queue.append((neighbour , dist[neighbour]))
        

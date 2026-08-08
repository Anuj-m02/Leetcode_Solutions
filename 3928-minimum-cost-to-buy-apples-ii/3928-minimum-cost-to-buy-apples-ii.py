from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:

        ans = [0]*(n)

        graph = defaultdict(list)
        for u , v , w , t in roads :
            graph[u].append((v,w,t))
            graph[v].append((u,w,t))

        def f(start_shop , prices , graph) :

            # curr_price , curr_shop , bought apple or not
            start = [(0 , start_shop , False) , (prices[start_shop] , start_shop , True)]

            dist = [[float("inf")] * 2 for _ in range(n)]


            dist[start_shop][1] = prices[start_shop]

            dist[start_shop][0] = 0

            res = dist[start_shop]

            while start :
                curr_price , curr_shop , bought = heapq.heappop(start)
                bought_indx = 1 if bought else 0

                if curr_price > dist[curr_shop][bought] :
                    continue

                if curr_shop == start_shop and bought :
                    return curr_price

                for neighbour_shop , weight , tax in graph[curr_shop]:
                    if not bought :
                        # two option buy now or buy later
                        if curr_price + weight < dist[neighbour_shop][0] :
                            dist[neighbour_shop][0] = curr_price + weight
                            heapq.heappush(start , (curr_price + weight , neighbour_shop , False))
                        
                        if curr_price + prices[neighbour_shop] + weight < dist[neighbour_shop][1] :
                            dist[neighbour_shop][1] = curr_price + prices[neighbour_shop] + weight
                            heapq.heappush(start , (curr_price + prices[neighbour_shop] + weight , neighbour_shop , True ))
                     
                    if bought :
                        # now return to start_shop
                        if curr_price + weight*tax < dist[neighbour_shop][1] :
                            heapq.heappush(start , (curr_price + weight*tax  , neighbour_shop , True))
                            dist[neighbour_shop][1] = curr_price + weight*tax
            
            return dist[start_shop][1]





        for shop in range(n):
            res = f(shop , prices , graph)
            ans[shop] = res
        
        return ans

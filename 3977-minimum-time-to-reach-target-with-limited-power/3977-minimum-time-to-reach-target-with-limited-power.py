from collections import defaultdict , deque
import heapq


class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:

        graph = defaultdict(list)

        for u , v , w in edges :
            graph[u].append((v,w))
        
        if source == target :
            return [0 , power]
        
        # dist has {(node , power)} = minimum time
        dist = defaultdict(lambda : float("inf"))

        heap = [(0 , -power , source)]
        dist[(source , power)] = 0

        best_time , best_power = float("inf") , -1

        while heap :
            curr_time , curr_power , curr_node = heapq.heappop(heap)
            curr_power = -curr_power

            if dist[(curr_node , curr_power)] != curr_time :
                continue

            if curr_time > best_time :
                break

            if curr_node == target :
                if best_time == float("inf") :
                    best_time = curr_time
                if curr_time == best_time :
                    best_power = max(best_power , curr_power)
                continue

            if curr_power < cost[curr_node] :
                continue

            new_power = curr_power - cost[curr_node] 

            for neighbour , weight in graph[curr_node] :
                new_time = curr_time + weight

                if new_time < dist[(neighbour  , new_power)] :
                    dist[(neighbour , new_power)] = new_time
                    heapq.heappush(heap , (new_time , -new_power , neighbour))

        if best_time == float('inf') :
            return [-1 , -1]

        return [best_time , best_power] 

        
        # heap = []
        # # {curr_node , rem_power}
        # time = [float("inf")]*n

        # heap.append((0 , -power , source))
        # time[source] = 0
        # ans = 0

        # while heap :
        #     curr_time , curr_power , curr_node = heapq.heappop(heap)
        #     curr_power = -curr_power
        #     if curr_node == target :
        #         ans = max(ans , curr_power)



        #     for neighbour in graph[curr_node] :
        #         rem_power = curr_power - cost[curr_node]
        #         if rem_power >= cost[neighbour] :
        #             heapq.heappush(heap , ((curr_time+1 , -rem_power , neighbour))
        

        # return [time[target] , ans ]




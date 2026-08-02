from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        grp_id_cntr = m
        for i in range(n) :
            if group[i] == -1 :
                group[i] = grp_id_cntr
                grp_id_cntr += 1
        
        item_graph = defaultdict(list)
        item_indegree = [0]*(n)

        grp_graph = defaultdict(list)
        grp_indegree = [0]*(grp_id_cntr)

        items_in_grp = defaultdict(list)
        for i in range(n):
            items_in_grp[group[i]].append(i)
        
        for curr_item in range(n) :
            curr_grp = group[curr_item]

            for prev_item in beforeItems[curr_item] :
                prev_grp = group[prev_item]
            
                if prev_grp == curr_grp :
                    item_graph[prev_item].append(curr_item)
                    item_indegree[curr_item] += 1
                
                else :
                    
                    grp_graph[prev_grp].append(curr_grp)
                    grp_indegree[curr_grp] += 1

        # topo sort inside each grp
        sorted_grp_items = {}

        for grp_id , items in items_in_grp.items() :

            queue = deque([u for u in items if item_indegree[u] == 0])

            sorted_items = []

            while queue :
                node = queue.popleft()
                sorted_items.append(node)
                for neighbour in item_graph[node] :
                    item_indegree[neighbour] -= 1
                    if item_indegree[neighbour] == 0 :
                        queue.append(neighbour)

            if len(sorted_items) != len(items) :
                return []
            
            sorted_grp_items[grp_id] = sorted_items
        
        #topo sort now for graph

        queue = deque([g for g in range(grp_id_cntr) if grp_indegree[g] == 0])
        sorted_grps = []

        while queue :
            curr_grp = queue.popleft()
            sorted_grps.append(curr_grp)
            for neighbour_grp in grp_graph[curr_grp] :
                grp_indegree[neighbour_grp] -= 1
                if grp_indegree[neighbour_grp] == 0 :
                    queue.append(neighbour_grp)
        
        if len(sorted_grps) != grp_id_cntr :
            return []
        
        res = []
        for grp in sorted_grps :
            res.extend(sorted_grp_items.get(grp , []))
        
        return res
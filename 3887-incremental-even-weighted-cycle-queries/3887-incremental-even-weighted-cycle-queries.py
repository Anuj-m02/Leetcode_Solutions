from collections import defaultdict
from typing import List

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        parent = list(range(n))
        size = [1]*(n)
        parity = [0]*(n) # parity from node to its parent

        def find(node) :
            # return parent[node] , parity[node]
            if parent[node] == node :
                return node , 0
            root , parity_node = find(parent[node])
            parity[node] = (parity[node] + parity_node)%2
            parent[node] = root

            return parent[node] , parity[node]
        
        def union(x , y , w) :
            parent_x , parity_x = find(x)
            parent_y , parity_y = find(y)
            if parent_x == parent_y :
                return

            new_parity = (parity_x + parity_y + w)%2 
            if size[parent_x] < size[parent_y] :
                parent[parent_x] = parent_y
                size[parent_y] += size[parent_x]
                parity[parent_x] = new_parity
            else :
                parent[parent_y] = parent_x
                size[parent_x] += size[parent_y]
                parity[parent_y] = new_parity

        ans = 0

        for u , v , w in edges :

            root_u , parity_u = find(u)
            root_v , parity_v = find(v)

            # same_component
            if root_u == root_v :
                if (parity_u + parity_v)%2 == w :
                    ans += 1
            
            else :
                val = (parity_u + parity_v + w)%2
                union(u , v , w)
                ans += 1
        
        return ans




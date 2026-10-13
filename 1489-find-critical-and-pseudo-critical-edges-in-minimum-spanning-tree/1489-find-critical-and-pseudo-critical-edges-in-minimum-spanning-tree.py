from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.size[xr] < self.size[yr]:
            self.parent[xr] = yr
            self.size[yr] += self.size[xr]
        else:
            self.parent[yr] = xr
            self.size[xr] += self.size[yr]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: add index to each edge
        for i, e in enumerate(edges):
            e.append(i)

        # Step 2: sort edges by weight
        edges.sort(key=lambda x: x[2])

        # Helper: Kruskal with optional skip/include
        def kruskal(skip=-1, force=-1):
            dsu = DSU(n)
            weight = 0
            edges_used = 0

            # If forcing one edge
            if force != -1:
                u, v, w, _ = edges[force]
                if dsu.union(u, v):
                    weight += w
                    edges_used += 1

            for i, (u, v, w, _) in enumerate(edges):
                if i == skip:
                    continue
                if dsu.union(u, v):
                    weight += w
                    edges_used += 1
                if edges_used == n - 1:
                    break

            return weight if edges_used == n - 1 else float("inf")

        # Step 3: get MST base weight
        base_weight = kruskal()

        critical, pseudo = [], []

        # Step 4: check each edge
        for i, (u, v, w, idx) in enumerate(edges):
            if kruskal(skip=i) > base_weight:
                critical.append(idx)
            elif kruskal(force=i) == base_weight:
                pseudo.append(idx)

        return [critical, pseudo]

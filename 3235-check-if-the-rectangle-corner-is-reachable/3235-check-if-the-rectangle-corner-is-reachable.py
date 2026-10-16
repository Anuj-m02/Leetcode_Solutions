# class Solution:
#     def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        
#         n = len(circles)

#         # create graph with n+4 vertices
#         graph = defaultdict(list)

#         # 0 ..n-1 are cricles , n -> upperedge , n+1 -> rigthedge , n+2 loweredge , n+3 leftedge

#         # ADD EDGE IF THERY INTERSECT OR TOUCH


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

    def connected(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:
        n = len(circles)
        
        # Virtual nodes for the boundaries
        TOP = n
        RIGHT = n + 1
        BOTTOM = n + 2
        LEFT = n + 3
        
        dsu = DSU(n + 4)

        # 1. Check if start (0,0) or end (xCorner, yCorner) is inside any circle
        for cx, cy, r in circles:
            if (cx ** 2 + cy ** 2 <= r ** 2) or ((cx - xCorner) ** 2 + (cy - yCorner) ** 2 <= r ** 2):
                return False

        # 2. Connect circles to borders and to other circles
        for i in range(n):
            x1, y1, r1 = circles[i]

            # Connect circle i to boundaries (if it intersects within boundary range)
            if abs(y1 - yCorner) <= r1 and 0 <= x1 <= xCorner:
                dsu.union(i, TOP)
            if abs(x1 - xCorner) <= r1 and 0 <= y1 <= yCorner:
                dsu.union(i, RIGHT)
            if abs(y1) <= r1 and 0 <= x1 <= xCorner:
                dsu.union(i, BOTTOM)
            if abs(x1) <= r1 and 0 <= y1 <= yCorner:
                dsu.union(i, LEFT)

            # Connect circle i to circle j if they intersect inside or on rectangle boundaries
            for j in range(i + 1, n):
                x2, y2, r2 = circles[j]
                
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                r_sum_sq = (r1 + r2) ** 2
                
                # Check if circles touch or overlap
                if dist_sq <= r_sum_sq:
                    # Check if the overlap occurs inside the rectangle domain
                    if x1 * r2 + x2 * r1 < (r1 + r2) * xCorner and \
                       y1 * r2 + y2 * r1 < (r1 + r2) * yCorner:
                        dsu.union(i, j)

        # 3. Check for blocking boundary combinations
        if dsu.connected(TOP, BOTTOM) or \
           dsu.connected(LEFT, RIGHT) or \
           dsu.connected(TOP, RIGHT) or \
           dsu.connected(LEFT, BOTTOM):
            return False

        return True
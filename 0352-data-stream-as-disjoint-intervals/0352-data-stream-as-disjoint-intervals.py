from typing import List

class SummaryRanges:

    def __init__(self):
        self.parent = {}
        # Maps the root of a component to its interval boundaries: [min_val, max_val]
        self.intervals = {}
        # Keeps track of numbers already added to avoid duplicate processing
        self.visited = set()

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Merge root_v into root_u
            self.parent[root_v] = root_u
            
            # Expand the interval boundaries of the new combined component
            self.intervals[root_u][0] = min(self.intervals[root_u][0], self.intervals[root_v][0])
            self.intervals[root_u][1] = max(self.intervals[root_u][1], self.intervals[root_v][1])
            
            # Since root_v is no longer a root, remove its interval record
            del self.intervals[root_v]

    def addNum(self, value: int) -> None:
        # Ignore duplicates
        if value in self.visited:
            return
            
        # Initialize the new number as its own disconnected component
        self.visited.add(value)
        self.parent[value] = value
        self.intervals[value] = [value, value]
        
        # Connect with the left neighbor if it exists
        if (value - 1) in self.visited:
            self.union(value, value - 1)
            
        # Connect with the right neighbor if it exists
        if (value + 1) in self.visited:
            self.union(value, value + 1)

    def getIntervals(self) -> List[List[int]]:
        # self.intervals only contains active roots, meaning it strictly holds 
        # the fully merged disjoint intervals. We just need to return them sorted.
        return sorted(self.intervals.values())
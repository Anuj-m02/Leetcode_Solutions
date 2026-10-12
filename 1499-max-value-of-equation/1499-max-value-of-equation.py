class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        
        n = len(points)
        max_heap = []
        # (-(yi-xi) , xi)
        max_val = float("-inf")

        for x,y in points :

            while max_heap and x - max_heap[0][1] > k :
                heapq.heappop(max_heap)
            
            if max_heap :
                max_val = max(max_val , -max_heap[0][0] + x + y)
            
            heapq.heappush(max_heap , (-(y-x) , x))
        
        return max_val
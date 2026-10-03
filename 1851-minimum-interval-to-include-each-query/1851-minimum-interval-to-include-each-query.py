class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        
        n = len(intervals)
        intervals.sort()
        m = len(queries)
        sorted_indx = sorted(range(m) , key = lambda i : queries[i])

        res , heap , i = [-1]*(m) , [] , 0

        for indx in sorted_indx :
            q = queries[indx]

            while i < n and intervals[i][0] <= q :
                heapq.heappush(heap , (intervals[i][1] - intervals[i][0] + 1 , intervals[i][1]))
                i += 1
            
            # print(heap)
            while heap and heap[0][1] < q :
                heapq.heappop(heap)

            # print(heap)
            if heap :
                res[indx] = heap[0][0]

        return res 
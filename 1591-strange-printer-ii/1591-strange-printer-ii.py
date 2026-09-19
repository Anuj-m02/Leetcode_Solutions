class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        
        n , m = len(targetGrid) , len(targetGrid[0])


        # for each colour get leftest , rightest , upest , downest points of that colour maens that much region was coloured by that colour

        bounds = {}
        for row in range(n):
            for col in range(m):
                colour = targetGrid[row][col]
                if colour not in bounds :
                    bounds[colour] = [row , row , col , col]
                else :
                    bounds[colour][0] = min(bounds[colour][0] , row)
                    bounds[colour][1] = max(bounds[colour][1] , row)
                    bounds[colour][2] = min(bounds[colour][2] , col)                    
                    bounds[colour][3] = max(bounds[colour][3] , col)
        
        graph = {colour : set() for colour in bounds}
        indegree = {colour : 0 for colour in bounds}

        for colour , (min_r , max_r , min_c , max_c) in bounds.items():
            for row in range(min_r , max_r + 1):
                for col in range(min_c , max_c + 1) :
                    other_colour = targetGrid[row][col]
                    if other_colour != colour :
                        if other_colour not in graph[colour] :
                            graph[colour].add(other_colour)
                            indegree[other_colour] += 1

        queue = deque([colour for colour in bounds if indegree[colour] == 0])
        cnt = 0

        while queue :
            curr_colour = queue.popleft()
            cnt += 1
            for neighbour in graph[curr_colour] :
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0 :
                    queue.append(neighbour)
        
        return cnt == len(bounds)




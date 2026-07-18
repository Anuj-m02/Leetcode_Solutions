from collections import defaultdict
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for u,v,t in edges :
            graph[u].append((v,t))
            graph[v].append((u,t))
        max_quality = 0
        n = len(values)
        def dfs(node , time_left , visited , curr_quality):
            nonlocal max_quality
            if node == 0 :
                max_quality = max(max_quality, curr_quality)
            for neighbour , cost in graph[node] :
                if time_left - cost >= 0 :
                    first_visit = neighbour not in visited
                    if first_visit :
                        visited.add(neighbour)
                        dfs(neighbour , time_left - cost , visited , curr_quality + values[neighbour])
                        visited.remove(neighbour)
                    else :
                        dfs(neighbour , time_left - cost , visited , curr_quality )


        visited = set()
        visited.add(0)
        # dfs( node , time_left , visited set , node value)
        dfs(0 ,maxTime , visited , values[0])
        return max_quality
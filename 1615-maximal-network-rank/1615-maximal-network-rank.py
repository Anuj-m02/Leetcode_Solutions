class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        
        degree = [0]*(n)
        graph = defaultdict(list)

        for u,v in roads :
            degree[u] += 1
            degree[v] += 1
            graph[u].append(v)
            graph[v].append(u)
        

        max_rank = 0

        for i in range(n) :
            for j in range(i+1 , n) :

                curr_rank = degree[i] + degree[j]

                if j in graph[i] :
                    curr_rank -= 1
                
                max_rank = max(max_rank , curr_rank)

        return max_rank
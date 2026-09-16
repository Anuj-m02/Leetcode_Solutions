class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(len(scores)) :
            graph[i] = sorted(graph[i] , key = lambda x : scores[x] , reverse = True)[:4]
        
        max_score = -1

        for u,v in edges :
            for w in graph[u]:
                for x in graph[v] :

                    if w != v and x != u and w != x :
                        curr_score = scores[w] + scores[x] + scores[u] + scores[v]
                        max_score = max(max_score , curr_score)
        
        return max_score
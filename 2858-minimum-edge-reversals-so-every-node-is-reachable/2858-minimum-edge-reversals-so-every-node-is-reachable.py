class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)
        for u,v in edges :
            graph[u].append((v,0)) # original
            graph[v].append((u,1)) # reverse cost 1
        
        ans = [0]*(n)

        # lets root the tree at node 0 
        def dfs1(node , parent) :
            for neighbour , cost in graph[node] :
                if neighbour == parent :
                    continue
                ans[0] += cost
                dfs1(neighbour , node)
        
        dfs1(0,-1)

        # rerooting dp
        def dfs2(node , parent) :
            for neighbour , cost in graph[node] :
                if neighbour == parent :
                    continue
                if cost == 0 :
                    ans[neighbour] = ans[node] + 1
                else :
                    ans[neighbour] = ans[node] - 1
                
                dfs2(neighbour , node)
        
        dfs2(0,-1)

        return ans


        
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        nxt = list(range(1,n+1))
        nxt[n-1] = -1
        curr_dist = n-1
        ans = []
        
        for u , v in queries :

            if nxt[u] == -1 or nxt[u] >= v :
                ans.append(curr_dist)
            
            else :

                curr = nxt[u]
                while curr != v :
                    nxt[curr] , curr = -1 , nxt[curr]
                    curr_dist -= 1
                
                nxt[u] = v
                ans.append(curr_dist)
            
                # curr = u
                # while curr < v :
                #     temp = nxt[curr]
                #     curr_dist -= 1
                #     curr = temp
                
                # curr_dist += 1
                # nxt[u] = v

            # ans.append(curr_dist)
        
        return ans





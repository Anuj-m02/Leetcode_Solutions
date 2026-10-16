class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        
        n , m = len(grid1) , len(grid1[0])

        cnt = 0

        for i in range(n) :
            for j in range(m) :
                if grid2[i][j] == 1 :
                    queue = deque([(i , j)])
                    grid2[i][j] = 0
                    is_island = True

                    while queue :
                        r , c = queue.popleft()

                        if grid1[r][c] == 0 :
                            is_island = False
                        
                        for dr , dc in [(-1,0) , (1,0) , (0,-1) , (0,1)] :
                            nr , nc = r + dr , c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid2[nr][nc] == 1 :
                                grid2[nr][nc] = 0
                                queue.append((nr , nc))
                    
                    if is_island :
                        cnt += 1
        
        return cnt

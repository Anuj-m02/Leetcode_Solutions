class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        n , m = len(grid) , len(grid[0])

        val = {0 : 4 , 1 : 3 , 2 : 2  , 3 : 1  , 4 : 0}

        dirs = [(0,1) , (1,0) , (-1,0) , (0,-1)]
        ans = 0
        for i in range(n):
            for j in range(m) :

                if grid[i][j] == 1 :
                    cnt = 0
                    for dx , dy in dirs :
                        new_i , new_j = i + dx , j + dy
                        if 0 <= new_i < n and 0 <= new_j < m :
                            if grid[new_i][new_j] ==  1 :
                                cnt += 1
                    
                    ans += val[cnt]

        return ans

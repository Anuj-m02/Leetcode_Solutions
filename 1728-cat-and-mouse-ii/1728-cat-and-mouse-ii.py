class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:

        n , m = len(grid) , len(grid[0])

        dirs = [(1,0) , (-1,0) , (0,1) , (0,-1)]
        mouse_pos , cat_pose = None , None
        available = 0

        for i in range(n):
            for j in range(m) :
                if grid[i][j] != "#" :
                    available += 1
                if grid[i][j] == "M" :
                    mouse_pos = (i,j)
                if grid[i][j] == "C" :
                    cat_pos = (i,j)
        
        @lru_cache(maxsize=None)
        def dp(turn , mouse_pos , cat_pos) :

            if turn > 2*available :
                return False
            
            if turn%2 == 0 :
                # mouse turn
                x , y = mouse_pos
                for dx , dy in dirs :
                    for jump in range(mouseJump + 1) :
                        new_x , new_y = x + dx*jump , y + dy*jump
                        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] != "#" :
                            if dp(turn+1 , (new_x , new_y) , cat_pos) or grid[new_x][new_y] == "F" :
                                return True
                        
                        else :
                            break
                
                return False

            else :
                # cat's turn
                x , y = cat_pos
                for dx , dy in dirs :
                    for jump in range(catJump+1) :
                        new_x , new_y = x + dx*jump , y + dy*jump
                        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] != "#" :
                            if not dp(turn+1 , mouse_pos , (new_x, new_y)) or (new_x , new_y) == mouse_pos or grid[new_x][new_y] == "F" :
                                return False
                        else :
                            break
                
                return True
            
        return dp(0 , mouse_pos , cat_pos)
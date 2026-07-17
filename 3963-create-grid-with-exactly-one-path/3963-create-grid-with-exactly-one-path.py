class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        grid = [(["#"]*n) for _ in range(m)]

        col = 0
        row = 0

        # if m == 1 :
        #     return [(".")*n]
        
        # if n == 1 :
        #     return [(".")*m]


        for i in range(n) :
            grid[0][i] = "."
        
        for i in range(m) :
            grid[i][n-1] = "."



        ans = []
        for row in grid :
            ans.append("".join(row))
        
        return ans

class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        
        # (0,0) and (m-1 , n-1) needs to be "."


        if m == 1 or n == 1 :
            if k == 1 :
                return ["." * n for _ in range(m)]
            
            return []
        
        temp = {
            1 : [["."]],
            2 : [[".." , ".."]] ,
            3 : [[".." , ".." , ".."] , ["..." , "..."]] ,
            4 : [[".." , ".." , ".." , ".."] , ["...." , "...."] , ["..#" , "..." , "#.."]]
        }

        for t in temp[k] :
            row , col = len(t) , len(t[0])
            if row <= m and col <= n :
                res = [["#"]* n for _ in range(m)]

                for i in range(row):
                    for j in range(col):
                        res[i][j] = t[i][j]

                for i in range(row , m):
                    res[i][col-1] = "."
                for j in range(col , n):
                    res[m-1][j] = "."

                return ["".join(row) for row in res]

        return []        
        

            

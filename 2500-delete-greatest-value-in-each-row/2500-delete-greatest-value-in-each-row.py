class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        

        n , m = len(grid) , len(grid[0])

        total = 0
        for col in range(m) :
            temp = 0
            for row in range(n) :
                curr_row = grid[row]
                maxi = max(curr_row)
                grid[row][curr_row.index(maxi)] = -1
                
                temp = max(temp , maxi)
            

            total += temp
        
        return total

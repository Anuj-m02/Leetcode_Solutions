class Solution:
    def countCommas(self, n: int) -> int:
        
        if n < 1000 :
            return 0
        
        # since n less than 1e5
        return (n-1000) + 1
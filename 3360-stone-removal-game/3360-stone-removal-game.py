class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        turn = 1
        curr = 10
        while n >= curr and curr > 0 :
            n -= curr
            turn = 1 - turn
            curr -= 1
        
        return turn == 0 
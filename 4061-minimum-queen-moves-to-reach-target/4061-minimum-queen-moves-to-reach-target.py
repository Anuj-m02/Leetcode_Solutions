class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        
        if source == target :
            return 0
        
        a,b = source
        c,d = target

        if a == c or b == d or abs(a-c) == abs(b-d) :
            return 1

        return 2
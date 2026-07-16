class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        
        res = 0
        for num in nums :
            s = str(num)
            res += s.count(str(digit))
        
        return res
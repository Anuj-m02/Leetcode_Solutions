class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        

        maxi , total = 0 , 0

        for nums in gain :
            total += nums
            maxi = max(maxi , total)
        
        return maxi
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        
        cnt1 , cnt2 = 0 , 0
        for indx , val in enumerate(nums) :

            if val > 0 :
                cnt1 += 1
            
            elif val < 0 :
                cnt2 += 1
            
        
        return max(cnt1 , cnt2)

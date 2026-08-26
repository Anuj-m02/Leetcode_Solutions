class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        mini_neg = 0
        n = len(nums)
        curr = 0 
        for i in range(n):
            curr += nums[i]
            if curr < mini_neg :
                mini_neg = curr
        
        return abs(mini_neg)+1


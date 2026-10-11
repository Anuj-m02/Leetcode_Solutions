class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        
        cnt = 0
        prev = nums[-1]
        n = len(nums)

        for i in range(n-2 , -1  , -1) :

            if nums[i] > prev :
                
                k = nums[i] // prev
                if nums[i]%prev :
                    k += 1
                cnt += k-1
                prev = nums[i]//k
            
            else :
                prev = nums[i]
        
        return cnt
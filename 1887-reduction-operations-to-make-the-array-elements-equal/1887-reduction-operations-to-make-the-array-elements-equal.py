class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        
        n = len(nums)

        nums.sort()
        ops = 0
        up_steps = 0

        for i in range(1 , n) :
            if nums[i] != nums[i-1] :
                up_steps += 1
            
            ops += up_steps
        
        return ops
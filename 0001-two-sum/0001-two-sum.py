class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target :
        #             return [i,j]
        
        d = {}
        total = 0
        for i in range(n):
            curr = nums[i]
            rem = target-curr
            if rem in d :
                return [d[rem] , i]
            
            d[curr] = i
        
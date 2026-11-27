class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # d = {}
        # for i in range(n):
        #     if nums[i] not in d :
        #         d[nums[i]] = 1
        #     else :
        #         d[nums[i]] += 1
        # return max(d)

        candidate = None
        cnt = 0
        for num in nums :
            if cnt == 0 :
                candidate = num
            
            cnt += 1 if num == candidate else -1
        
        return candidate
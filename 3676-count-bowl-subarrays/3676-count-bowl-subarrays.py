class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        stack = []
        cnt = 0


        for indx , val in enumerate(nums) :
            while stack and nums[stack[-1]] < val :
                stack.pop()
                if stack :
                    cnt += 1
            
            stack.append(indx)
        
        return cnt
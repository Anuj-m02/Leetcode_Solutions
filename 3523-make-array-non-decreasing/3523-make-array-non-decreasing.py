class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        
        n = len(nums)

        stack = []
        for i in range(n-1 , -1 , -1) :
            curr_ele = nums[i]
            while stack and stack[-1] < curr_ele :
                stack.pop()
            stack.append(nums[i])
            
        return len(stack[::-1])

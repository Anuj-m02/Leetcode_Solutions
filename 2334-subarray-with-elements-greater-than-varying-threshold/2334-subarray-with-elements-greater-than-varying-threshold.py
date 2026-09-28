class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:
        
        # min(subarr) > k * threshold

        n = len(nums)
        nums.append(0)
        stack = []

        for i in range(n+1) :
            while stack and nums[stack[-1]] > nums[i] :
                top_indx = stack.pop()
                val = nums[top_indx]

                left_bound = stack[-1] if stack else -1
                right_bound = i

                k = right_bound-left_bound-1

                if val*k > threshold :
                    return k
            
            stack.append(i)
        
        return -1
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        
        n = len(nums)

        left , right = 0 , n-1
        cnt = 0
        while left < right :

            while left < right and nums[right] == 0 :
                right -= 1

            if nums[left] == 0 and left < right :
                nums[left], nums[right] = nums[right] , nums[left]
                cnt += 1
                right -= 1

            left += 1
        
        return cnt
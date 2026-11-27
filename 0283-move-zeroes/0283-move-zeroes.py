class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer to track the position of the next non-zero element
        # n = len(nums)
        # k = 0
        # z = 0
        # for i in range(n):
        #     if nums[i] != 0 :
        #         nums[k] = nums[i]
        #         k += 1
        #     else :
        #         z += 1
        # nums[k:n] = [0]*z

        n = len(nums)
        k = 0
        for i in range(n) :
            if nums[i] != 0 :
                if i != k :
                    nums[k] , nums[i] = nums[i] ,nums[k]
                k += 1
        
        # return nums
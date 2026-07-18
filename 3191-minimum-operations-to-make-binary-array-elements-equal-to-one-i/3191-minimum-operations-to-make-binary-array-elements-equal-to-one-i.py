class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)

        indx = 0
        cnt = 0

        while indx < n :
            if nums[indx] == 0 :
                cnt += 1
                if indx+3 <= n :
                    for j in range(3):
                        nums[indx+j] = 1-nums[indx+j]
            indx += 1  
        
        print(nums)
        if nums.count(1) != n :
            return -1

        return cnt 
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        

        n = len(nums)

        k_sums = [0]*(n-k+1)
        curr_sum = sum(nums[:k])
        k_sums[0] = curr_sum
        for i in range(1 , n-k+1) :
            curr_sum += nums[i+k-1] - nums[i-1]
            k_sums[i] = curr_sum

        @lru_cache(maxsize=None)
        def dp(indx , cnt) :
            if cnt == 3 :
                return 0
            
            if indx >= len(k_sums) :
                return float("-inf")
            
            take = k_sums[indx] + dp(indx+k , cnt + 1)

            skip = dp(indx+1 , cnt)


            return max(take , skip)
        

        res = []
        indx = 0
        cnt = 0

        while indx <= len(k_sums) and cnt < 3 :
            take = k_sums[indx] + dp(indx+k , cnt+1)
            skip = dp(indx+1 , cnt)

            if take >= skip :
                res.append(indx)
                indx += k
                cnt += 1
            else :
                indx += 1
        
        return res




             
            

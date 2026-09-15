class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        
        n = len(nums)


        if n == 0 :
            return []

        suf_min = [0]*(n)
        suf_min[-1] = nums[-1]

        for i in range(n-2 , -1 , -1) :
            suf_min[i] = min(nums[i] , suf_min[i+1])
        
        ans = [0]*(n)
        pref_max = 0
        comp_max = 0
        start = 0

        for i in range(n) :
            pref_max = max(pref_max , nums[i])
            comp_max = max(comp_max , nums[i])

            if i == n-1 or pref_max <= suf_min[i+1] :
                for j in range(start , i+1) :
                    ans[j] = comp_max
                start = i+1
        
        return ans
        # @lru_cache(maxsize=None)
        # def dp(indx) :

        #     maxi = nums[indx]

        #     for j in range(indx+1 , n):
        #         if nums[j] < nums[indx] :
        #             maxi = max(maxi , dp(j))
            
        #     for j in range(indx) :
        #         if nums[j] > nums[indx] :
        #             maxi = max(maxi , dp(j))
            
        #     return maxi
        
        # return [dp(i) for i in range(n)]
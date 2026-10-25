class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)

        @lru_cache(maxsize=None)
        def dp(indx , arr) :
            if indx >= n :
                return 0
            
            ans = 0
            curr1 , curr2  = nums1[indx] , nums2[indx]
            if arr == 1 :
                prev = nums1[indx-1]
            else :
                prev = nums2[indx-1]
            
            if curr1 >= prev :
                ans = max(ans , 1 + dp(indx+1 , 1))

            if curr2 >= prev :
                ans = max(ans , 1 + dp(indx+1 , 2))
            
            
            return ans
        

        max_len = 1
        for i in range(n) :
            max_len = max(max_len , 1 + dp(i+1 , 1) , 1 + dp(i+1 , 2))
        
        return max_len




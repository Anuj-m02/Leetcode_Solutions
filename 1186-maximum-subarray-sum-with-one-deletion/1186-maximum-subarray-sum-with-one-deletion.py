class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        
        n = len(arr)


        @lru_cache(maxsize=None)
        def dp(indx , opt) :

            if indx >= n :
                return float("-inf")
            
            # take this ele and continue subarry
            ans = arr[indx] + max(0 , dp(indx+1 , opt))

            # delete curr element 
            if opt :
                ans = max(ans , dp(indx+1 , False ))
            
            return ans
        
        max_sum = max(arr)
        for indx in range(n) :
            max_sum = max(max_sum , dp(indx , True))
        
        return max_sum
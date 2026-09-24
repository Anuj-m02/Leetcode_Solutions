class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        
        max_val = {}
        n = len(arr)

        for i in range(n):
            curr_max = arr[i]
            for j in range(i,n) :
                curr_max = max(curr_max , arr[j])
                max_val[(i,j)] = curr_max
        
        @lru_cache(maxsize=None)
        def dp(left , right) :

            if left >= right :
                return 0
            
            res = float("inf")
            for k in range(left , right) :

                cost = max_val[(left , k)] * max_val[(k+1 , right)] + dp(left , k) + dp(k+1 , right)

                res = min(res , cost)
            
            return res
        
        return dp(0 , n-1)
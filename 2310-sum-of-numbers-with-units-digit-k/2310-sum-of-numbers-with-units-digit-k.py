class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
        n = len(str(num))

        candidates = []
        for x in range(1 , num+1) :
            if x%10 == k :
                candidates.append(x)
        


        @lru_cache(maxsize=None)
        def dp(total) :

            if total == 0 :
                return 0
            
            if total < 0 :
                return float("inf")
            
            ans = float("inf")
            for new_num in candidates :
                ans = min(ans , 1 + dp(total-new_num))
            
            return ans


        ans = dp(num)
        if ans != float("inf") :
            return ans
        else :
            return -1

class Solution:
    def deleteString(self, s: str) -> int:
        
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(indx) :
            if indx >= n :
                return 0
            
            # delete entire string
            ans1 = 1
            ans2 = 0
            # find seq where repaeting

            rem_len = n-indx
            for k in range(1 , rem_len//2 + 1):
                sub_string = s[indx : indx+k]
                new_string = s[indx+k : indx+2*k]

                if sub_string == new_string :
                    ans2 = max(ans2 , 1 + dp(indx+k))

            return max(ans1 , ans2) 

        return dp(0)
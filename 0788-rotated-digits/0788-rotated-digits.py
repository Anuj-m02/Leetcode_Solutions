class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        # since n is upto 1e4 so 4 pos _ _ _ _

        s = str(n)
        invalid = {3,4,7}

        d = {2:5 , 5:2 , 6:9 , 9:6}

        @cache
        def dp(indx , is_less , has_diff):

            if indx == len(s) :
                return 1 if has_diff else 0
            
            upper_bound = 9 if is_less else int(s[indx])

            cnt = 0

            for digit in range(upper_bound + 1) :
                if digit in invalid :
                    continue
                
                nxt_is_less = is_less or (digit < upper_bound)
                nxt_has_diff = has_diff or (digit in d)

                cnt += dp(indx+1 , nxt_is_less , nxt_has_diff)
            
            return cnt
        
        return dp(0 , False , False)

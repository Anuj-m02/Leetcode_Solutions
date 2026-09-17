class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        

        # low = low
        # high = high

        def count(num) :
            s = str(num)
            n = len(str(num))


            # 9 * 20 * 2^9 * 2
            @lru_cache(maxsize=None)
            def dp(indx , cnt_even , cnt_odd , rem , is_limit , is_started):

                # print(curr_num)

                # if curr_num and int(curr_num) < low and int(curr_num) > high :
                #     return 0

                if indx >= n :
                    if is_started and cnt_even == cnt_odd and rem == 0 :
                        return 1
                    else :
                        return 0
                
                ans = 0
                limit = int(s[indx]) if is_limit else 9
                # lower = 0 if is_started else 1

                for digit in range(0 , limit+1) :
                    nxt_limit = is_limit and (digit == limit)
                    if not is_started and digit == 0 :
                        ans += dp(indx+1 , cnt_even , cnt_odd  , rem , nxt_limit , False)
                    else :
                        
                        nxt_even = cnt_even + (1 if digit%2 == 0 else 0)
                        nxt_odd = cnt_odd + (1 if digit%2 == 1 else 0)
                        nxt_rem = (rem*10 + digit)%k
                        ans += dp(indx+1 , nxt_even , nxt_odd , nxt_rem , nxt_limit , True)
                
                return ans
            
            return dp(0 , 0 , 0 , 0 , True , False)
        
        return count(high)-count(low-1)
from functools import lru_cache
from collections import defaultdict , deque , Counter
import heapq

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:

        n , m = len(low) , len(high)
        mod = 10**9 + 7

        # first get n digits 
        # then get n+1 , n+2 ,..upto m digits
        # like for each case we have _ _ _ _ like n spaces and we keep cnt of dp(indx , prev)

        def solve(s) :
            length = len(s) 

            @lru_cache(maxsize=None)
            def dp(indx , prev , is_tight , is_started) :
                if indx == length :
                    return 1 if is_started else 0

                ans = 0
                upper = int(s[indx]) if is_tight else 9

                for num in range(0 , upper+1) :
                    nxt_tight = is_tight and (num == upper)

                    if not is_started :
                        if num == 0 :
                            # leading zero , so not start
                            ans += dp(indx+1 , -1 , nxt_tight , False)%mod
                        else :
                            # firt non zero digit start
                            ans += dp(indx+1 , num , nxt_tight , True)%mod
                    
                    else :

                        if abs(num-prev) == 1 :
                            ans += dp(indx+1 , num , nxt_tight , True)%mod
                
                return ans%mod
            
            return dp(0 , -1 , True , False)


        def is_stepping(s) :
            for i in range(1 , len(s)) :
                if abs(int(s[i]) - int(s[i-1])) != 1 :
                    return False
            return True
        
        return (solve(high) - solve(low) + is_stepping(low))%mod

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        
        n = len(s)

        candid = list(range(n+1))

        c = frozenset(candid)
        mod = int(1e9)+7

        @cache
        def dp(indx , prev_rank) :

            if indx == n :
                return 1
            

            curr = s[indx]
            ans = 0

            if curr == "D" :
                for nxt_rank in range(0,prev_rank) :
                    ans += dp(indx+1 , nxt_rank) % mod
            
            if curr == "I" :
                for nxt_rank in range(prev_rank , n-indx) :
                    ans += dp(indx+1 , nxt_rank) % mod
            
            return ans
        

        cnt = 0
        for start in range(n+1) :
            cnt += dp(0 , start) % mod
        
        return cnt%mod


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])

        @lru_cache(maxsize=None)
        def dp(indx , prev_indx) :

            if indx >= m :
                return 0
            
            # delete this indx
            ans = 1 + dp(indx+1 , prev_indx)
            
            # pick this indx
            chk = True
            if prev_indx != -1 :
                for i in range(n) :
                    if strs[i][indx] < strs[i][prev_indx] :
                        chk = False
                        break

            if chk :
                ans = min(ans , dp(indx+1 , indx)) 
            

            return ans

        return dp(0 , -1)
            

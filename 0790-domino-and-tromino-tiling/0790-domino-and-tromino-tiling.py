class Solution:
    def numTilings(self, n: int) -> int:
        
        mod = int(1e9)+7

        @cache
        def dp(indx , state) :

            if indx > n :
                return 0
            
            if indx == n :
                if state == 0 :
                    return 1
                else :
                    return 0
            

            if state == 0 :

                # fully covered at column i-1
                # vertical dominio dp(i+1 , 0)
                # two horizontal domino dp(i+2 , 0)
                # tromuno 2 orientation choice 2 * dp(i+2 , 1)

                res = (dp(indx+1 , 0) + dp(indx+2 , 0) + 2*dp(indx+2 , 1))%mod
            
            else :
                # partially covered at column i-1
                # complete with trimono dp(i+1 , 0)
                # extend with horizontal dominio dp(i+1 , 1)

                res = (dp(indx+1 , 0) + dp(indx+1 , 1))% mod
            
            return res
        
        return dp(0,0)


            
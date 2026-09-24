class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        n = len(pattern)

        def dp(indx , prev_num , s) :

            if indx >= n :
                return s
            
            ans = "9"*10
            if pattern[indx] == "I" :
                for i in range(prev_num+1 , 10) :
                    if str(i) not in s :
                        ans = min(ans , dp(indx+1 , i , s + str(i)))
            
            if pattern[indx] == "D" :
                for i in range(1 , prev_num) :
                    if str(i) not in s :
                        ans = min(ans , dp(indx+1 , i , s + str(i)))
            
            return ans

        res = "9"*10
        for i in range(1 , 10) :
            res = min(res , dp(0 , i , str(i)))
        
        return res

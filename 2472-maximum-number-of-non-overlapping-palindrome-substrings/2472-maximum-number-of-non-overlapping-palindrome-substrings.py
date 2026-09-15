class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        n = len(s)

        def is_palindrome(left , right):
            return s[left:right+1] == s[left:right+1][::-1]

        @lru_cache(maxsize=None)
        def dp(indx) :

            if indx >= n :
                return 0
            
            # dont take this indx
            ans = dp(indx+1)
            # not_take = dp(indx+1 , -1)

            # option 2
            for j in range(indx+k-1 , min(indx+k+1 , n)):
                if is_palindrome(indx , j) :
                    ans = max(ans , 1 + dp(j+1))
                    break
            
            return ans
        
        return dp(0)

            # # take
            # if prev_indx == -1 :
            #     # starting
            #     take = dp(indx+1 , indx)
            # else :
            #     take = dp(indx+1 , prev_indx)

            #     if indx - prev_indx >= k :
            #         if s[prev_indx:indx+1] == s[prev_indx:indx+1][::] :
            #             return 1
            
            # return max(take , not_take)
        
        return dp(0 , -1)

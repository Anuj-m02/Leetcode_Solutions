class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        mod = int(1e9)+7

        changes = {
            "a" : ["e"] , 
            "e" : ["a" , "i"],
            "i" : ["a" , "e" , "o" , "u"],
            "o" : ["i" , "u"] , 
            "u" : ["a"]
        }

        @cache
        def dp(indx , prev_vowel) :

            if indx == n :
                return 1
            
            total = 0

            for nxt_vowel in changes[prev_vowel] :
                total += dp(indx+1 , nxt_vowel)%mod
            
            return total%mod
        
        ans = 0
        for v in ["a" , "e" , "i" , "o" , "u"] :
            ans += dp(1 , v)%mod
        
        return ans%mod


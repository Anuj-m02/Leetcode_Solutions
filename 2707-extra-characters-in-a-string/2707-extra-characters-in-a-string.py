class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        n = len(s)
        dict_set = set(dictionary)

        @lru_cache(maxsize=None)
        def dp(indx) :

            if indx == n :
                return 0
            
            min_extra = 1 + dp(indx+1)

            # check 
            for word in dict_set :
                if indx + len(word) <= n : 
                    if s[indx : indx+len(word)] == word :
                        min_extra = min(min_extra , dp(indx+len(word)))
            
            return min_extra
        
        return dp(0)
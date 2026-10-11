class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        

        n = len(words)

        def valid(i , j) :
            if groups[i] == groups[j] or len(words[i]) != len(words[j]) :
                return False
            
            return sum(c1 != c2 for c1,c2 in zip(words[i] , words[j])) == 1
        
        @lru_cache(maxsize=None)
        def dp(indx) :

            best_suffix = []
            for j in range(indx+1 , n) :
                if valid(indx , j) :
                    cand = dp(j)
                    if len(cand) > len(best_suffix) :
                        best_suffix = cand
            
            return [words[indx]] + best_suffix
        
        res = []
        for indx in range(n) :
            cand = dp(indx)
            if len(cand) > len(res) :
                res = cand
        
        return res
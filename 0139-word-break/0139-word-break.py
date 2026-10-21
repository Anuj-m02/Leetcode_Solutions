class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # wordDict.sort()
        word_set = set(wordDict)
        dp = {}
        def f(indx):
            if indx == n :
                return True
            if indx in dp :
                return dp[indx]

            for word in wordDict :
                if indx + len(word) <= n and s[indx:indx+len(word)] == word :
                    if f(indx+len(word)) :
                        dp[indx] = True
                        return True
            dp[indx] = False
            return False

        return f(0)
        

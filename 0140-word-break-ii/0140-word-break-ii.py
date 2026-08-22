class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n = len(s)
        word_set = set(wordDict)

        ans = []
        path = []

        def dp(indx , prev_indx):

            if indx == n :
                if prev_indx == n :
                    ans.append(" ".join(path))
                return
            
            # dont space here
            dp(indx+1 , prev_indx )

            # space here
            curr_word = s[prev_indx:indx+1]
            if curr_word in word_set :
                path.append(curr_word)
                dp(indx+1 , indx+1)
                path.pop()
            
        
        dp(0,0)

        return ans




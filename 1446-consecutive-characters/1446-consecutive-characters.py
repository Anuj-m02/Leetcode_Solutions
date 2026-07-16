class Solution:
    def maxPower(self, s: str) -> int:
        
        n = len(s)

        maxi = 0
        cnt = 1

        if len(s) == 1 :
            return 1

        for i in range(n-1):
            if s[i] == s[i+1] :
                cnt += 1
            else :
                cnt = 1
            
            maxi = max(maxi , cnt)
        
        return maxi
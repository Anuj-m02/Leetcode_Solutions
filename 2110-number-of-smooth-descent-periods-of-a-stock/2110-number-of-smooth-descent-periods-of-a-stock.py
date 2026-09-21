class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        
        n = len(prices)

        ans = n
        prev = -1
        cnt = 0
        for indx in range(n) :
            curr = prices[indx]
            if prev - curr  == 1 :
                cnt += 1
            else :
                cnt = 0
            
            ans += cnt
            prev = curr

        return ans

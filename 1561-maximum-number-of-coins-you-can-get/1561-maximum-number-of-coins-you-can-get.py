class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        # 8 7 4 2 2 1

        piles.sort(reverse=True)
        n = len(piles) 
        cnt = 0
        ans = 0
        indx = 1

        # 9 8 7 6 5 4 3 2 1

        while indx < n and cnt < n//3:
            cnt += 1
            ans += piles[indx]
            indx += 2
        
        return ans




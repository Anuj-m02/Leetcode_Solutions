class Solution:
    def minSwaps(self, s: str) -> int:
        

        n = len(s)
        cnt_open , cnt_close = 0 , 0 
        max_imbalance = 0
        for indx in range(n) :
            curr = s[indx]

            if curr == "[" :
                cnt_open += 1
            
            else :
                cnt_close += 1
            
            # swap needed
            if cnt_close > cnt_open :
                max_imbalance = max(max_imbalance , cnt_close - cnt_open)
        
        return (max_imbalance+1)//2
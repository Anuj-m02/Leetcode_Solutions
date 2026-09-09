class Solution:
    def countCommas(self, n: int) -> int:
        
        # n is till 1e15 , 1,000 1,000,000 4 7 10 13 16

        if n <= 999 :
            return 0
        
        total = 0
        start = 1000
        end = start*1000 - 1
        cnt = 1

        while start <= n:
            num = min(n , end) - start + 1
            total += cnt*num

            if end > n :
                break
            
            start *= 1000
            end = start*1000 - 1
            cnt += 1
        
        return total
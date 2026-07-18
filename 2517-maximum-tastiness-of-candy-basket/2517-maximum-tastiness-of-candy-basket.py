class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()

        n = len(price)

        low = 0 
        high = int(1e9)

        def check(mid , k , price) :
            prev , cnt , indx = price[0] , 1 , 1
            while cnt < k and indx < len(price) :
                if price[indx] - prev >= mid :
                    cnt += 1
                    prev = price[indx]
                indx += 1
            
            return cnt == k


        ans = 0
        while low <= high :
            mid = (low+high)//2
            if check(mid , k , price) :
                ans = max(ans , mid)
                low = mid+1
            else :
                high = mid-1
        
        return ans

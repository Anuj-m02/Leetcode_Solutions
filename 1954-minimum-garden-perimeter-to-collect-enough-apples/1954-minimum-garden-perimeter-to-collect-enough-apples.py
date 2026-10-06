# class Solution:
#     def minimumPerimeter(self, neededApples: int) -> int:
        
        # # apples increasing as 0 , 9 , 9+16 , 9+16+25 , 
        # apples = [0]*(int(1e5)+7)
        # for i in range(3 , int(1e5)+1) :
        #     apples[i] = apples[i-1] + i*i
        
        # indx = bisect.bisect_left(apples , neededApples)
        # return indx*4

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right = 1, 10**6
        
        while left < right:
            mid = (left + right) // 2
            apples = 2 * mid * (mid + 1) * (2 * mid + 1)
            
            if apples >= neededApples:
                right = mid
            else:
                left = mid + 1
                
        return 8 * left
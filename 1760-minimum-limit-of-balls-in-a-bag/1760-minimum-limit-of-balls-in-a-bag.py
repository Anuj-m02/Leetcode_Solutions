class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        n = len(nums)

        def check(mid) :
            # maximum no of balls in bag less than equal to mid
            ops = 0
            for n in nums :
                ops += math.ceil(n / mid) - 1
                if ops > maxOperations :
                    return False
            
            return True



        low = 1
        high = int(1e10)
        ans = 0
        while low <= high :
            mid = (low+high)//2
            if check(mid) :
                ans = mid
                high = mid-1
            else :
                low = mid+1
        
        return ans
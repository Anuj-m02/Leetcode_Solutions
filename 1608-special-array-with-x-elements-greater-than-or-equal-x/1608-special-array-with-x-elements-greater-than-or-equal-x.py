class Solution:
    def specialArray(self, nums: list[int]) -> int:
        
        n = len(nums)
        nums.sort()

        def check(x) :
            indx = bisect.bisect_left(nums , x)
            # ele greater than or equal to x
            return n - indx == x 

        for x in range(n+1) :
            if check(x) :
                return x
        
        return -1
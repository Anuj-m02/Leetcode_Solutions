class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(x) :
            if x == 1 :
                return 0
            
            if x%2 == 0 :
                return 1 + dp(x//2)

            else :
                return 1 + dp(x*3 + 1)
                    

        nums = list(range(lo , hi+1))
        nums.sort(key = lambda x : (dp(x) , x))

        return nums[k-1]
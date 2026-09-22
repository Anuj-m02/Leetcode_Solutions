class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(nums)

        def check(mid) :
            diff = [0]*(n+1)

            for i in range(mid) :
                left , right , val = queries[i]
                diff[left] += val
                diff[right+1] -= val
            
            curr_sum = 0
            for i in range(n) :
                curr_sum += diff[i]
                if curr_sum < nums[i] :
                    return False
            
            return True


        low , high = 0 , len(queries)
        ans = -1
        while low <= high :
            mid = (low+high)//2

            if check(mid) :
                ans = mid
                high = mid-1
            else :
                low = mid+1
        
        return ans

        for left , right , val in queries :
            diff[left] += val
            if right + 1 < n :
                diff[right+1] -= val
         


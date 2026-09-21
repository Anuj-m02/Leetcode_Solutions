class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        maxi = max(nums)
        n = len(nums)

        left , right  = 0 , 0
        d = defaultdict(int)
        cnt = 0

        for right in range(n) :
            curr = nums[right]
            d[curr] += 1
            
            while d[maxi] >= k :
                d[nums[left]] -= 1
                left += 1
            
            cnt += left
            
        
        return cnt
from collections import defaultdict  ,deque , Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        left = 0

        count = defaultdict(int)
        wind_count = defaultdict(int)

        for right in range(n) :
            curr = nums[right]
            
            wind_count[curr] += 1

            if right-left+1 > k :
                wind_count[nums[left]] -= 1
                if wind_count[nums[left]] == 0 :
                    del wind_count[nums[left]]
                left += 1
            
            if right - left + 1 == k :
                for num in wind_count :
                    count[num] += 1
        
        ans = -1
        for num , cnt in count.items() :

            if cnt == 1 :
                ans = max(ans , num)
        
        return ans


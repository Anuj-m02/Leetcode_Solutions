class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        left , right = 0 , 0
        freq = defaultdict(int)
        ans = float("inf")
        total_sum = 0


        for right in range(n) :
            curr = nums[right]

            if freq[curr] == 0 :
                total_sum += curr
            
            freq[curr] += 1

            while total_sum >= k :
                ans = min(ans , right-left+1)

                freq[nums[left]] -= 1
                if freq[nums[left]] == 0 :
                    total_sum -= nums[left]
                
                left += 1



        
        if ans == float("inf") :
            return -1
        else :
            return ans


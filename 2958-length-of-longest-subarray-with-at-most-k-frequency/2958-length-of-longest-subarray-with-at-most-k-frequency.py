class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        left , right = 0 , 0
        d = defaultdict(int)
        maxi = 0

        for right in range(n) :
            curr = nums[right]

            d[curr] += 1
            while d[curr] > k :
                left_ele = nums[left]
                d[left_ele] -= 1
                if d[left_ele] == 0 :
                    del d[left_ele]
                left += 1
            
            maxi = max(maxi , right-left+1)
        
        return maxi

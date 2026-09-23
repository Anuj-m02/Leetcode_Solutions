class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        n = len(nums)

        prefix_sum = [0]*(n)
        suffix_sum = [0]*(n)
        prefix_sum[0] , suffix_sum[n-1] = nums[0] , nums[n-1]

        for indx in range(1 , n) :
            prefix_sum[indx] = prefix_sum[indx-1] + nums[indx]
        
        for indx in range(n-2 , -1 , -1) :
            suffix_sum[indx] = suffix_sum[indx+1] + nums[indx]
        

        suffix_rev_sum = suffix_sum[::-1]

        ans = float("inf")
        # only suffix
        indx = bisect.bisect_left(suffix_rev_sum , x)
        if indx < n and suffix_rev_sum[indx] == x :
            ans = min(ans , indx+1)
        
        for i in range(n) :
            p_sum = prefix_sum[i]
            p_len = i+1

            # only prefix
            if p_sum == x :
                ans = min(ans , p_len)
            
            # both prefix and suffix
            elif p_sum < x :
                rem = x - p_sum
                indx = bisect.bisect_left(suffix_rev_sum , rem)

                if indx < n and suffix_rev_sum[indx] == rem :
                    s_len = indx+1
                    if p_len + s_len <= n :
                        ans = min(ans , p_len + s_len)
        

        return ans if ans != float("inf") else -1
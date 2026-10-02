# class Solution:
#     def minimizeMax(self, nums: List[int], p: int) -> int:
        
#         n = len(nums)
#         nums.sort()

#         if 2*p >= n :
#             return -1
        

#         def check(mid) :
#             cnt = 0

#             # left , right = 0 , n-1
#             # while left <= right :

#             #     if abs(nums[left] - nums[right]) <= mid :
#             #         cnt += 1
#             #         right -= 1
                
#             #     else :
#             #         left += 1
            
#             # return cnt >= p
#             indx = 0
#             while indx < n-1 :
#                 if nums[indx+1] - nums[indx] <= mid :
#                     cnt += 1
#                     indx += 2
#                 else :
#                     indx += 1
            
#             return cnt >= p

#             # for indx in range(1 , n-1) :
#             #     diff1 = abs(nums[indx]-nums[indx-1])
#             #     diff2 = abs(nums[indx+1] - nums[indx])

#             #     if min(diff1 , diff2) <= mid :
#             #         cnt += 1
            
#             # return cnt >= p 


        
#         low , high = 0 , max(nums)
#         ans = high
#         while low <= high :
#             mid = (low+high)//2
#             if check(mid) :
#                 ans = mid
#                 high = mid-1
            
#             else :
#                 low = mid+1
        
#         return ans

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)

        def check(mid: int) -> bool:
            cnt = 0
            i = 0
            while i < n - 1:
                # If adjacent pair difference is within mid threshold
                if nums[i + 1] - nums[i] <= mid:
                    cnt += 1
                    i += 2  # Skip both elements used in this pair
                else:
                    i += 1  # Move to the next adjacent pair
            return cnt >= p

        low = 0
        high = nums[-1] - nums[0]  # Max possible difference after sorting
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1  # Try searching for a smaller maximum difference
            else:
                low = mid + 1  # Threshold too strict, increase mid

        return ans
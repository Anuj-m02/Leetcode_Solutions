# class Solution:
#     def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        
#         n = len(arr)

#         left , right = 0, 0
#         total = 0
#         d = defaultdict(int)
#         cnt = 0

#         for right in range(n) :
#             curr = arr[right]
#             d[curr] += 1
#             total += curr

#             curr_avg = total // (right-left+1)

#             if right-left+1 == k :
#                 if total/k >= threshold :
#                     cnt += 1
                
#                 d[arr[left]] -= 1
#                 total -= arr[left]
#                 left += 1
        
#         return cnt

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        left, total, cnt = 0, 0, 0

        for right in range(n):
            total += arr[right]

            # Use while ONLY to shrink the window back to size k if it exceeds k
            while right - left + 1 > k:
                total -= arr[left]
                left += 1

            # Now the window size is guaranteed to be <= k
            if right - left + 1 == k and total / k >= threshold:
                cnt += 1

        return cnt
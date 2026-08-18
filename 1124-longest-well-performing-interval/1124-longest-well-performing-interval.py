# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
        
#         n = len(hours)

#         tiring , non_tiring = 0 , 0
#         left = 0
#         right = 0
#         ans = 0
#         score = 0
#         seen = {0 : -1}

#         prefix = [0]*(n+1)

#         for i in range(n) :
#             if hours[i] > 8 :
#                 prefix[i+1] = prefix[i] + 1 
            
#             else :
#                 prefix[i+1] = prefix[i] - 1
        

#         # find the last indx where prefix is posiitve
#         last_indx = 0
#         for i in range(n) :
#             if prefix[i] > 0 :
#                 last_indx = max(last_indx , i)
        
#         return last_indx



#         # for indx , h in enumerate(hours) :

#         #     if h > 8 :
#         #         score += 1
#         #     else :
#         #         score -= 1
            
#         #     if score > 0 :
#         #         ans = indx+1
            
#         #     elif (score-1) in seen :
#         #         ans = max(ans , indx - seen[score-1])
            
#         #     if score not in seen :
#         #         seen[score] = indx
        
#         # return ans
                


#         # for right in range(n) :

#         #     if hours[right] > 8 :
#         #         tiring += 1
#         #     else :
#         #         non_tiring += 1
            
#         #     if tiring > non_tiring :
#         #         ans = max(ans , right-left+1)
            
#         #     while non_tiring > tiring :
#         #         if hours[left] > 8 :
#         #             tiring -= 1
#         #         else :
#         #             non_tiring -= 1
#         #         left += 1
        
#         # return ans


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        
        # Step 1: Compute prefix sums (+1 for >8, -1 for <=8)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if hours[i] > 8 else -1)
        
        # print(prefix_sum)
            
        # Step 2: Build a strictly decreasing stack of candidate starting indices
        stack = []
        for i in range(n + 1):
            # print(stack)
            if not stack or prefix_sum[i] < prefix_sum[stack[-1]]:
                stack.append(i)
            
                
        ans = 0
        
        # Step 3: Iterate backwards from right to left to find the max length
        for right in range(n, -1, -1):
            while stack and prefix_sum[right] > prefix_sum[stack[-1]]:
                left = stack.pop()
                ans = max(ans, right - left)
                
        return ans
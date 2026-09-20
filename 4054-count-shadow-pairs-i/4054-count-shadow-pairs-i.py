class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        
        n = len(nums)

        # nxt smaller element 
        # (value , count)
        stack = []
        smaller_cnt = 0
        ans = 0

        for x in nums :
            
            # pop all elements greater than x
            while stack and stack[-1][0] > x :
                val , cnt = stack.pop()
                smaller_cnt -= cnt
            
            # print(stack)
            # print(ans)

            # cnt pairs ending at indx x
            eql_cnt = stack[-1][1] if stack and stack[-1][0] == x else 0
            ans += smaller_cnt - eql_cnt

            if stack and stack[-1][0] == x :
                stack[-1][1] += 1
            else :
                stack.append([x,1]) 
            
            smaller_cnt += 1
        
        return ans

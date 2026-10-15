class Solution:
    def numSteps(self, s: str) -> int:
        
        curr_num = int(s , 2)
        cnt = 0
        while curr_num != 1 :
            if curr_num % 2 == 1 :
                curr_num += 1
            else :
                curr_num = curr_num//2
            
            cnt += 1
        
        return cnt

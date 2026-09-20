class Solution:
    def reverseDegree(self, s: str) -> int:
        
        cnt = 0
        for indx , char in enumerate(s) :
            rev , og = ord("z") - ord(char) + 1 , indx+1 
            cnt += rev*og
        
        return cnt

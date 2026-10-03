class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        n = len(s)
        maxi = -1
        cnt_zero , cnt_one = 0 , 0
        while cnt_zero < n//2 + 2 :

            if "0"*cnt_zero + "1"*cnt_one in s :
                maxi = max(maxi , cnt_zero + cnt_one)

            cnt_zero += 1
            cnt_one += 1

        return maxi

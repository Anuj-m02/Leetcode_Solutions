class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        # maximum 9 we can take , then 8 then 7
        freq = [0]*(10)
        
        if sum > num*9 :
            return ""
        
        res = []
        for _ in range(num) :
            digit = min(9 , sum)
            res.append(str(digit))
            sum -= digit
        
        if sum > 0 :
            return ""
        
        return "".join(res)

        # curr_digit = 9
        # indx = 0
        # res = ""
        # while indx < num :
        #     while curr_digit > sum :
        #         curr_digit -= 1
            
        #     # if indx == 0 and curr_digit == 0 :
        #     #     if num > 1:
        #     #         return ""
        #     #     else :
        #     #         return "0"

        #     sum -= curr_digit
        #     res += str(curr_digit)
        
        # return res

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        s = str(n)
        total , prod = 0 , 1
        for i in range(len(s)) :
            curr = int(s[i])
            total += curr
            prod = prod*curr
        
        if n%(total + prod) == 0  :
            return True
        
        return False
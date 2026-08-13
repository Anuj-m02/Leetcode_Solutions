import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        left , right = 0,0
        n , m = len(str1) , len(str2)

        gcd = math.gcd(n,m)

        a , b = n//gcd , m//gcd

        temp1 , temp2 = str1[:gcd] , str2[:gcd]

        if temp1*(a) == str1 and temp2*(b) == str2 and temp1 == temp2 :
            return temp1
        
        return ""
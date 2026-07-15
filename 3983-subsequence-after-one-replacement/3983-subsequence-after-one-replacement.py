class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        
        n , m = len(s) , len(t)

        if len(s) > len(t) :
            return False
        
        elif len(s) == len(t) :
            c = 0
            for i in range(n):
                if c > 1 :
                    return False
                if s[i] != t[i] :
                    c += 1
            
            if c > 1 :
                return False
            return True
        
        else :

            i , j = 0 ,0
             #(no replacement , replacment)

            for char in t :
                if s[j] == char :
                    j += 1
                
                if s[i] == char :
                    i += 1
                else :
                    j = max(j , i+1)
                
                if i == n or j == n :
                    return True
            
            return False
            




            # left , right = 0 , 0
            # chk = False
            # while left < n and right < m :

            #     if s[left] != t[right] :
            #         if not chk :
            #             chk = True
            #             left += 1
            #             right += 1
            #         else :
            #             right += 1
                
            #     elif s[left] == t[right] :
            #         left += 1
            #         right += 1
            
            # if left != n :
            #     return False
            # return True


                
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(s):
            cnt = 1
            ans = ""
            for i in range(1,len(s)):
                if s[i] == s[i-1] :
                    cnt += 1
                else :
                    ans += (str(cnt) + str(s[i-1]))
                    cnt = 1
            ans += str(cnt)+s[-1]
            return ans

                

        @lru_cache(None)
        def f(n):
            if n == 1 :
                return "1"
            else :
                return rle(f(n-1))
        
        return f(n)
        
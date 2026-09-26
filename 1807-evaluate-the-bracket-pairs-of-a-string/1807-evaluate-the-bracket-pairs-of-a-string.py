class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        n , m = len(s) , len(knowledge) 
        d = defaultdict()

        for key,val in knowledge :
            d[key] = val
        
        ans = ""

        i = 0
        while i < n :
            val = s[i]

            if val == "(" :
                for j in range(i+1 , n) :
                    if s[j] == ")" :
                        break

                substring = s[i+1:j]
                if substring in d :
                    new_str = d[substring]
                else :
                    new_str = "?"
                
                i = j+1

            else :
                new_str = val
                i += 1

            ans += new_str 

        return ans        

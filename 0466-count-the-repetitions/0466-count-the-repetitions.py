class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        
        str1 = s1*n1
        str2 = s2*n2


        # string = str2*m from str1


        len1 , len2 = len(s1) , len(s2)

        @lru_cache(maxsize=None)
        def solve(s2_indx) :
            s2_cnt = 0
            for char in s1 :
                if char == s2[s2_indx] :
                    s2_indx += 1
                    if s2_indx == len2 :
                        s2_cnt += 1
                        s2_indx = 0
            
            return s2_cnt , s2_indx
        
        total_s2_cnt = 0
        curr_s2_indx = 0

        for _ in range(n1) :
            s2_matched , curr_s2_indx = solve(curr_s2_indx)
            total_s2_cnt += s2_matched
        
        return total_s2_cnt // n2

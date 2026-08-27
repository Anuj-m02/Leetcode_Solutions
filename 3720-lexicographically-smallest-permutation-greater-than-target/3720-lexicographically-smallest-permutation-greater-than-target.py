from itertools import permutations
from collections import defaultdict , deque , Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        

        d1 , d2 = Counter(s) , Counter(target)

        n , m = len(s) , len(target)

        indx = 0
        while indx < n and d1[target[indx]] > 0 :
            d1[target[indx]] -= 1
            indx += 1
        

        for i in range(indx , -1 , -1) :
            if i < indx :
                d1[target[i]] += 1
            
            if i == n :
                continue
            
            for ch in range(ord(target[i]) +1 , ord("z") + 1) :

                char = chr(ch)

                if d1[char] > 0 :
                    d1[char] -= 1
                
                    res = list(target[:i]) + [char]

                    for avail_char in sorted(d1.keys()) :
                        res.extend([avail_char] * d1[avail_char])
                    
                    return "".join(res)
        
        return ""

            

        # temp = []

        # for perm in permutations(s) :
        #     temp.append("".join(perm))
        
        # temp.sort()
        # for strings in temp :
        #     if strings > target :
        #         return strings
        
        # return ""



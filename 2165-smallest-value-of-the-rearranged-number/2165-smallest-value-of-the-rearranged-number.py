from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def smallestNumber(self, num: int) -> int:

        digits = []
        temp = abs(num)
        s = str(temp)
        for i in s :
            digits.append(i)
        
        if num == 0 :
            return 0
        
        # we got all unique digits
        
        if num < 0 :
            # num is less than zero means desceing order of digits
            digits.sort(reverse=True)
            s = ""
            for i in digits :
                s += i
            return -1*(int(s))
        
        if num > 0 :

            # num is greater than zero leading zeros not allowed so first smaller value thereafeter asceing order
            digits.sort()
            first_non_zero = -1
            for i in digits :
                if i != "0" :
                    first_non_zero = i
                    digits.remove(first_non_zero)
                    break
            s = str(first_non_zero)
            for i in digits :
                s += i
            
            return int(s)


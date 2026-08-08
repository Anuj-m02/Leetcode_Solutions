from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minOperations(self, n: int, m: int) -> int:

        def prime(num) :
            if num < 2 :
                return False
            for i in range(2 ,  int(num**0.5) + 1 ) :
                if num % i == 0 :
                    return False
            return True
        
        if prime(n) or prime(m):
            return -1

        dist = defaultdict(lambda : float("inf"))

        dist[n] = n

        # curr_dist , curr_num
        heap  = [(n,n)]
        while heap :
            curr_dist , curr_num = heapq.heappop(heap)

            if curr_num == m :
                return curr_dist

            if dist[curr_num] < curr_dist :
                continue
            
            s = list(str(curr_num))
            for i in range(len(s)) :
                orig_char = s[i]
                digit = int(orig_char)

                next_dig = []
                if digit < 9 :
                    next_dig.append(digit+1)
                if digit > 0 :
                    next_dig.append(digit-1)
                
                for new_digit in next_dig :
                    s[i] = str(new_digit)
                    temp = int("".join(s))

                    # if len(str(temp)) != len(s) :
                    #     continue
                    
                    if not prime(temp) :
                        new_dist = curr_dist + temp
                        if new_dist < dist[temp] :
                            dist[temp] = new_dist
                            heapq.heappush(heap , (new_dist , temp))
                
                s[i] = orig_char
        
        return -1



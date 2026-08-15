from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        # bulls in and correct pos
        # cows in and wrong pos

        bulls , cows = 0,0

        n = len(secret)

        ptr1 , ptr2 = 0 , 0 
        # d = defaultdict(int)
        # for i in secret :
        #     d[i] += 1
        skip = set()

        while ptr1 < n :
            if secret[ptr1] == guess[ptr2] :
                # d[secret[ptr1]] -= 1
                # if d[guess[ptr2]] == 0 :
                #     del d[guess[ptr2]]
                skip.add(ptr1)
                bulls += 1
            # else :
            #     if guess[ptr2] in d :
            #         d[guess[ptr2]] -= 1
            #         cows += 1
            #         if d[guess[ptr2]] == 0 :
            #             del d[guess[ptr2]]
            
            ptr1 += 1
            ptr2 += 1
        
        # we got bulls count

        ptr1 , ptr2 =  0, 0
        d = defaultdict(int)
        for indx , val in enumerate(secret) :
            if indx not in skip :
                d[val] += 1

        while ptr1 < n :
            if secret[ptr1] != guess[ptr2] :
                if guess[ptr2] in d :
                    d[guess[ptr2]] -= 1
                    cows += 1
                    if d[guess[ptr2]] == 0 :
                        del d[guess[ptr2]]
            
            ptr1 += 1
            ptr2 += 1
        



        return str(bulls) + "A" + str(cows) + "B"



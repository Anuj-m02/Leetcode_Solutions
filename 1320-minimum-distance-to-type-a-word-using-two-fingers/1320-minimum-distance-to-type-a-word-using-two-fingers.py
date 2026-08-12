from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        
        # precompute distance of all letter from A , distance of all letter from B in alphabeticalorderonly
        # A B C D E F
        # G H I J K L
        # M N O P Q R
        # S T U V W X
        # Y Z

        def get_pos(char) :
            indx = ord(char) - ord("A")
            return indx//6 , indx % 6

        graph = defaultdict(dict)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for char1 in alphabet :
            row1 , col1 = get_pos(char1)
            for char2 in alphabet :
                row2 , col2 = get_pos(char2)
                graph[char1][char2] = abs(row1-row2) + abs(col1-col2)

        n = len(word)

        # 26 * 26 * 300
        @lru_cache(None)
        def dp(indx , fing1 , fing2) :
            if indx == n :
                return 0
            
            # cost1 = type with fing1
            # cost2 = type with fing2
            cost1 = graph[fing1][word[indx]] + dp(indx+1 , word[indx] , fing2)
            cost2 = graph[fing2][word[indx]] + dp(indx+1 , fing1 , word[indx])

            return min(cost1 , cost2)
        



        # two fingers can be placed at any letter of word except first letter or first two letter

        ans = float("inf")
        for fing1 in range(n):
            for fing2 in range(n) :
                if (fing1 == 0 and fing2 == 1) or (fing1 == fing2) :
                    continue
                else :
                    res = dp(0 , word[fing1] , word[fing2])
                    ans = min(ans , res)

        return ans 


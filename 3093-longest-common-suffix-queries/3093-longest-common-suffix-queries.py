from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class TrieNode :
    def __init__(self) :
        self.children = {}
        self.best_indx = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        root = TrieNode()

        def is_better(new_indx , curr_indx) :
            if curr_indx == -1 :
                return True
            
            new_len = len(wordsContainer[new_indx])
            curr_len = len(wordsContainer[curr_indx])

            if new_len != curr_len :
                return new_len < curr_len
            
            return new_indx < curr_indx


        for indx , word in enumerate(wordsContainer) :
            node = root
            if is_better(indx , node.best_indx) :
                node.best_indx = indx
            
            for char in reversed(word) :
                if char not in node.children :
                    node.children[char] = TrieNode()

                node = node.children[char]
                if is_better(indx , node.best_indx) :
                    node.best_indx = indx
        
        ans = []
        for query in wordsQuery :
            node = root
            for char in reversed(query) :
                if char in node.children :
                    node = node.children[char]
                else :
                    break
            
            ans.append(node.best_indx)
        
        return ans
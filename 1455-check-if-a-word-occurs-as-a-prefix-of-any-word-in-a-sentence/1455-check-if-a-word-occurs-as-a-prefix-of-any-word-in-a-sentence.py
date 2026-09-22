class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        arr = sentence.split(" ")
        n = len(arr)

        for indx , word in enumerate(arr) :
            m = len(word)
            k = len(searchWord)
            if word[:k] == searchWord :
                return indx+1
        
        return -1
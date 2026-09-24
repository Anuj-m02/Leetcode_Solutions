class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        rev_indx = -1
        for indx , char in enumerate(word) :
            if char == ch :
                rev_indx = indx
                break
        
        return word[:rev_indx+1][::-1] + word[rev_indx+1:]

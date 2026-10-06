class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        
        n = len(sentences)
        maxi = -1

        for i in range(n) :

            arr = sentences[i].split(" ")
            maxi = max(maxi , len(arr))
        
        return maxi
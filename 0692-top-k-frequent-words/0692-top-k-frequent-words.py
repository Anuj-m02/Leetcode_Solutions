from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        count = Counter(words)

        heap = []
        for word , cnt in count.items() :
            heapq.heappush(heap , (-cnt , word))
        
        ans = []
        for i in range(k) :
            ans.append(heapq.heappop(heap)[1])
        
        return ans

from collections import defaultdict

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        ans = []

        prefix_map = defaultdict(list)

        for words in products :
            s = ""
            for indx in range(len(words)) :
                s += words[indx]
                prefix_map[s].append(words)
        
        s = ""
        for indx in range(len(searchWord)) :
            s += searchWord[indx]
            candidate = prefix_map[s]
            ans.append(candidate[:3])
        
        return ans




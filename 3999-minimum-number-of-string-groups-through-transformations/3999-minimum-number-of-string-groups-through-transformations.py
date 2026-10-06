

class Solution:
    def minimumGroups(self, words: List[str]) -> int:

        def get_min_hash(s) :
            l = len(s)
            hashes = []
            pw_l = 1
            h = 0
            for c in s :
                h = (h*27 + ord(c) - ord("a") + 1)%mod
                hashes.append(h)
                pw_l = pw_l*27 % mod
            
            pw = 1
            min_hash = float("inf")
            for i in range(l) :
                pw = pw*27 % mod
                min_hash = min(min_hash , (hashes[i] + hashes[-1]*pw - hashes[i]*pw_l) % mod)
            
            return min_hash

        mod = int(1e9) + 7

        n = len(words)
        max_len = max(len(w) for w in words)

        uniq = set()
        for w in words :
            uniq.add((get_min_hash(w[::2]), get_min_hash(w[1::2]))) 
        
        return len(uniq)
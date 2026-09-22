class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        n = len(s)

        # maximum poss length of subseq n//k

        # atlest k occurence of char
        d = Counter(s)
        candidates = []
        for key,val in d.items():
            if val >= k :
                candidates.append(key)
        
        candidates.sort(reverse=True)

        def valid(sub) :
            target = sub*k
            i = 0
            for char in s :
                if char == target[i]:
                    i += 1
                    if i == len(target) :
                        return True
            
            return False

        queue = deque([""])
        ans = ""

        while queue :
            curr = queue.popleft()

            for ch in candidates :
                nxt_sub = curr + ch
                if valid(nxt_sub) :
                    if len(nxt_sub) > len(ans) or (len(nxt_sub) == len(ans) and nxt_sub > ans) :
                        ans = nxt_sub
                    queue.append(nxt_sub)
        
        return ans
        
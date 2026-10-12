class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:

        freq = [0] * batchSize
        # remainders of batches

        for g in groups :
            freq[g % batchSize] += 1
        
        # 0 remainders means they got fresh baked
        happy_cnt = freq[0]

        initial_cnts = frozenset((r , freq[r]) for r in range(1 , batchSize) if freq[r] > 0)

        @lru_cache(maxsize=None)
        def dp(counts , rem) :
            if not counts :
                return 0
            
            max_happy = 0
            is_happy = 1 if rem == 0 else 0

            for r , count in counts :
                if count == 1 :
                    nxt_count = counts - {(r , count)}
                
                else :
                    nxt_count = (counts - {(r , count)}) | {(r , count-1)}
                
                nxt_rem = (rem + r)% batchSize
                max_happy = max(max_happy , is_happy + dp(nxt_count , nxt_rem))
            
            return max_happy
        
        return happy_cnt + dp(initial_cnts , 0)

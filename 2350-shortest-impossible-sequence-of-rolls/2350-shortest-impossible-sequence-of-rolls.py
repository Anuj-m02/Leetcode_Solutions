class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        
        # 1 : {2 , 3 , 4}
        # 2 : {1 , 3  ,4}
        # 3 : {2 , 4 , 1}
        # 4 : {1 , 2 , 3}
        # store in last_seen way


        last_seen = {}

        ans = 0
        seen = set()

        for indx , val in enumerate(rolls) :
            last_seen[val] = indx
            seen.add(val)

            if len(seen) == k :
                ans += 1
                seen.clear()
        
        return ans+1
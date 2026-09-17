class Solution:
    def maxProduct(self, s: str) -> int:
        
        n = len(s)

        @lru_cache(maxsize=None)
        def get_lps(available_indices) :
            if not available_indices :
                return 0
            
            indices = sorted(available_indices)
            if len(indices) == 1 :
                return 1
            
            first , last = indices[0], indices[-1]

            if s[first] == s[last] :
                return 2 + get_lps(frozenset(indices[1:-1]))
            
            else :
                return max(get_lps(frozenset(indices[1:])) ,
                            get_lps(frozenset(indices[:-1])))
        
        self.max_prod = 0

        def dfs(indx , sub1_chars , sub1_indices) :
            if indx == n :
                if sub1_chars and sub1_chars == sub1_chars[::-1] :
                    len1 = len(sub1_chars)

                    remaining_indices = frozenset(set(range(n)) - sub1_indices)
                    len2 = get_lps(remaining_indices)

                    self.max_prod = max(self.max_prod , len1*len2)
                
                return
            
            #INCLUDE
            # sub1_indices.add(indx)
            dfs(indx+1 , sub1_chars + s[indx] , sub1_indices | {indx})
            # sub1_indices.remove(indx)
            #EXCLUDE
            dfs(indx+1 , sub1_chars , sub1_indices)
        
        dfs(0 , "" , set())
        return self.max_prod



class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        

        # 22 pos 
        n1 , n2 = len(num1) , len(num2)
        max_indx = max(n1 , n2)
        min_indx = min(n1 , n2)
        mod = int(1e9)+7
        def count(num_str) :
            n = len(num_str)
            @lru_cache(maxsize=None)
            def dp(indx , curr_sum , is_limit) :

                if curr_sum > max_sum :
                    return 0
                
                if indx == n :
                    return 1 if min_sum <= curr_sum <= max_sum else 0
                
                upper_bound = int(num_str[indx]) if is_limit else 9
                ans = 0

                for digit in range(upper_bound+1):
                    nxt_limit = is_limit and (digit == upper_bound)
                    ans += dp(indx+1 , curr_sum + digit , nxt_limit)%mod
                
                return ans%mod
            
            return dp(0 , 0 , True)
        
        ans2 = count(num2)%mod
        ans1 = count(num1)%mod

        num1_sum = sum(int(d) for d in num1)
        is_num1_valid = 1 if min_sum <= num1_sum <= max_sum else 0

        return (ans2- ans1 + is_num1_valid)%mod


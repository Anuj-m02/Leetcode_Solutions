from collections import Counter



class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 1 :
            return n
        
        base1 , mod1 = 1315423911 , 1000000007
        base2 , mod2 = 2654435761 , 1000000009

        pow1 = [1]*(n+1)
        pow2 = [1]*(n+1)
        pref1 = [0]*(n+1)
        pref2 = [0]*(n+1)

        for indx , val in enumerate(nums) :
            x = val + 1
            
            pow1[indx+1] = (pow1[indx]*base1)%mod1
            pow2[indx+1] = (pow2[indx]*base2)%mod2
            
            pref1[indx+1] = (pref1[indx]*base1 + x)%mod1
            pref2[indx+1] = (pref2[indx]*base2 + x)%mod2
        
        def get_hash(left , right) :
            length = right-left
            h1 = (pref1[right] - pref1[left] * pow1[length])%mod1
            h2 = (pref2[right] - pref2[left] * pow2[length])%mod2
            return (h1 ,h2)
        
        def has_unique_of_len(length) :
            counts = Counter()
            for start in range(n-length+1) :
                counts[get_hash(start , start+length)] += 1
            
            return any(freq == 1 for freq in counts.values())
        

        low , high = 1 , n
        ans = n
        while low <= high :
            mid = (low+high)//2
            if has_unique_of_len(mid) :
                ans = mid
                high = mid-1
            else :
                low = mid+1

        return ans
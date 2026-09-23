class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:


        def check(mid) :
            r1 , r2 = r
            d1 , d2 = d
            lcm = math.lcm(r1,r2)

            # hrs where dron1 available
            cnt1_only = mid//r2 - mid//lcm
            # hrs where dron2 avail
            cnt2_only = mid//r1 - mid//lcm

            # where both drone avail
            shared = mid - (mid//r1) - (mid//r2) + (mid//lcm)

            rem1 = max(0 , d1 - cnt1_only)
            rem2 = max(0 , d2 - cnt2_only)

            return rem1 + rem2 <= shared





        low , high = 1 , int(4e9)
        ans = 0
        while low <= high :
            mid = (low+high)//2
            if check(mid) :
                ans = mid
                high = mid-1
            else :
                low = mid+1
        
        return ans
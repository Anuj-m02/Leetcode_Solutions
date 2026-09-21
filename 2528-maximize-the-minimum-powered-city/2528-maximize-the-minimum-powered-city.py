class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        

        n = len(stations)

        power = [0]*(n)
        window_sum = sum(stations[:min(n,r+1)])
        power[0] = window_sum

        for i in range(1,n) :
            if i+r < n :
                window_sum += stations[i+r]
            
            if i-r-1 >= 0 :
                window_sum -= stations[i-r-1]
            
            power[i] = window_sum
        
        low = min(power)
        high = sum(stations) + k
        ans = low

        def check(min_power_req , additional_stations) :
            window_power = sum(stations[:r])
            additions = [0]*(n)

            for i in range(n) :
                if i + r < n :
                    window_power += stations[i+r]
                
                if window_power < min_power_req :
                    needed = min_power_req - window_power
                    if needed > additional_stations :
                        return False
                
                    additions[min(n-1 , i+r)] += needed
                    window_power = min_power_req
                    additional_stations -= needed
                if i-r >= 0 :
                    window_power -= stations[i-r] + additions[i-r]

            return True    

        # def check(target) :
        #     # diffrence array mthd
        #     additions = [0]*(n+1)
        #     curr_added = 0
        #     needed_k = 0

        #     for i in range(n):
        #         curr_added += additions[i]
        #         curr_power = power[i] + curr_added

        #         if curr_power < target :
        #             diff = target - curr_power
        #             needed_k += diff
        #             if needed_k > k :
        #                 return False
                    
        #             curr_added += diff

        #             if i + 2*r + 1 < n :
        #                 additions[i + 2*r + 1] -= diff
            
        #     return True


        while low <= high :
            mid = (low+high)//2
            if check(mid , k) :
                ans = mid
                low = mid+1
            else :
                high = mid-1
        
        return ans

        # get prefix sum
        # then no_of_stations[indx] = prefix[indx+r] + prefix[indx-r]

        # once we get initiall no_of_Statoins
        # now we can add k power stations anywhere 
        # so lets do binary search on maximum minim power stations if check(mid)
        # check(mid) if k poerw station distributed optimially then return Truen or fLSE 

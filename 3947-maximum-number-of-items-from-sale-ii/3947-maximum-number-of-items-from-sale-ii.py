class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        
        n = len(items)

        max_factor = max(factor for factor , _ in items)
        min_price = min(price for _ , price in items)

        freq = [0]*(max_factor+1)
        for factor , _ in items :
            freq[factor] += 1
        
        multiples_cnt = [0]*(max_factor+1)
        for f in range(1 , max_factor+1) :
            if freq[f] :
                for mult in range(f , max_factor+1 , f) :
                    multiples_cnt[f] += freq[mult]
            

        boosted_by_price = defaultdict(int)
        for factor , price in items :
            gain = multiples_cnt[factor]-1
            if gain > 0 and price <= 2 * min_price :
                boosted_by_price[price] += gain
        

        min_heap = [(price , count) for price , count in boosted_by_price.items()]
        heapq.heapify(min_heap)

        total = 0
        while min_heap :
            price , count = heapq.heappop(min_heap)
            if budget < price :
                break
            
            take = min(count , budget//price)
            total += 2*take
            budget -= take*price


        total += budget//min_price
        return total 



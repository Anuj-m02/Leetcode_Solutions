from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:

        n = len(prices)
        m = len(discounts)

        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        j = 0 
        total = 0
        for i in range(n) :
            curr_price , new_price = prices[i] , prices[i]
            if j < m :
                curr_discount = discounts[j]
                new_price = (curr_price)*(100-curr_discount)/100
                j += 1
            total += new_price
        
        return total
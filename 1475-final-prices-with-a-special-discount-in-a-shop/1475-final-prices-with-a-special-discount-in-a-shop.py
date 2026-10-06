class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        
        n = len(prices)

        # next smaller element
        stack = []
        nse = [-1]*(n)

        for i in range(n) :

            while stack and prices[stack[-1]] >= prices[i] :
                indx = stack.pop()
                nse[indx] = i

            stack.append(i)
        
        # print(nse)
        res = []

        for i in range(n) :

            new_price = prices[i]
            if nse[i] != -1 :
                disc = prices[nse[i]]
                new_price = prices[i] - disc

            res.append(new_price)
        
        return res


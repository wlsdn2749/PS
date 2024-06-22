class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        profit = 0
        buy, sell = -1, -1

        for idx, item in enumerate(prices):
            print(profit)
            if buy >= 0:
                if sell < prices[idx]:
                    sell = prices[idx]
                elif sell > prices[idx]:
                    profit += sell - buy
                    sell = -1
                    buy = -1

            if buy == -1 or buy > prices[idx]:
                buy = prices[idx]

            
            if idx == len(prices) - 1 and sell > buy:
                profit += sell - buy

        return profit


            
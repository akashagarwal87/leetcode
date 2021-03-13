class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices): return 0
        isBought=False
        buyingDays=[]
        for i in range(len(prices) -1):
            # to buy or not to buy
            if len([x for x in prices[i+1:] if (x > prices[i])]) > 0:
                buyingDays.append(prices[i])
        
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
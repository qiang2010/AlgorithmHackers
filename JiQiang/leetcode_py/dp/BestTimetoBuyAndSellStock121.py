

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        tempMin = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit,prices[i]-tempMin)
            if prices[i] < tempMin:
                tempMin = prices[i]

        return maxProfit

if __name__ == '__main__':

    so = Solution()
    print(so.maxProfit([122,3,2,1000]))




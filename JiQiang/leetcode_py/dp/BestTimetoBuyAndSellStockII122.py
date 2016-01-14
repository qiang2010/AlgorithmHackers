

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        maxProfit = 0
        size = len(prices)
        for i in range(1,size):
            if prices[i] > prices[i-1]:
                maxProfit+=prices[i]-prices[i-1]
        return maxProfit

if __name__ == '__main__':

    so = Solution()
    print(so.maxProfit([122,3,2,1000]))




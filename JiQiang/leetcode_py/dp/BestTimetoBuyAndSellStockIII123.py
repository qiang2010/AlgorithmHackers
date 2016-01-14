

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        maxProfit = 0
        tempMin = prices[0]
        tempMax = prices[len(prices)-1]

        size = len(prices)

        leftMax = 0
        rightMax = 0
        tempLeftMax = [0]
        tempRightMax = [0]
        for i in range(1,size):
            curPro = prices[i] - tempMin
            if curPro > leftMax:
                leftMax = curPro
            tempLeftMax.append(leftMax)
            if tempMin > prices[i]:
                tempMin = prices[i]

            curPro = tempMax - prices[size-1-i]
            if rightMax < curPro:
                rightMax = curPro
            tempRightMax.append(rightMax)
            if tempMax < prices[size-i-i]:
                tempMax = prices[size-1-i]
        # print(tempLeftMax)
        # print(tempRightMax)
        for i in range(len(tempLeftMax)):
            maxProfit = max(maxProfit,tempLeftMax[i]+tempRightMax[size-1-i])
        return maxProfit

if __name__ == '__main__':

    so = Solution()
    pr = [2,1,2,0,1]
    #pr = [1,2]
    print(so.maxProfit(pr))






class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return -1
        if len(nums)==1:return 0
        step = 1
        maxPos = nums[0]
        i = 1
        while maxPos<len(nums)-1:
            tempPos =0
            while  i < maxPos+1 and i < len(nums):
                tempPos = max(tempPos,nums[i]+i)
                i+=1
            if tempPos <= maxPos:return -1
            maxPos = tempPos
            step+=1
        return step


if __name__ == '__main__':

    so = Solution()
    print(so.jump([1,2]))



class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:return False
        maxPos = nums[0]

        size = len(nums)
        for i in range(size):
            if maxPos >= size-1:return True
            if i < maxPos+1:
                m = nums[i]+i
                if m > maxPos:
                    maxPos = m
            else:return  False
        return  True
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:return False
        maxPos = 0
        size = len(nums)
        for i in range(size):
            if maxPos >= size-1:return True
            if i < maxPos+1:
                m = nums[i]+i
                if m > maxPos:
                    maxPos = m
            else:return False
        return  True
if __name__ == '__main__':

    so = Solution()
    print(so.canJump([3,2,1,0,4]))

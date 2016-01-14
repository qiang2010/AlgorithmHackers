

class Solution(object):
    def permute(self, nums):
        """
        全排列，给定的数都是唯一的，没有重复的。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.per(nums,0,len(nums)-1)
        return self.ans
    def per(self,nums,k,n):
        """

        :param nums: List[int] 要处理的数组
        :param k: int 当前要处理的数的位置
        :param ans: 最终的结果
        :param n: 数组的长度
        :return:
        """
        if k == n:
            tempAns = [ i  for i in nums]
            self.ans.append(tempAns)
            return
        j = k
        while j < n+1:
            self.swap(nums,k,j) # 交换
            self.per(nums,k+1,n)
            self.swap(nums,k,j) # 换回来
            j+=1

    def swap(self,nums,i,j):
        """
        交换 nums 在位置i和j上的数
        :param nums: List[int]
        :param i: int
        :param j:int
        :return:
        """
        if i == j:return
        a = nums[i]
        nums[i] = nums[j]
        nums[j] = a



if __name__ == '__main__':

    so = Solution()
    ans = so.permute([1,2])
    print(ans)
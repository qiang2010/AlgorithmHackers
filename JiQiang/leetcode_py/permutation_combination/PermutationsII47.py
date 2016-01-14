

class Solution(object):
    def permuteUnique(self, nums):
        """
        全排列，给定的数都是唯一的，没有重复的。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.per(nums,0,ans)
        return  ans

    def per(self,nums,k,ans):
        """
        :param nums: List[int]
        :param k: int
        :param ans:  List[List[int]]
        :return:
        """
        if k == len(nums)-1:
            one = [i for i in nums]
            ans.append(one)
            return
        j = k
        while j < len(nums):
            if j > k and nums[j] == nums[k]: j+=1;continue
            if self.dup(nums,k,j) : j+=1;continue
            self.swap(nums,k,j)
            self.per(nums,k+1,ans)
            self.swap(nums,k,j)
            j+=1

    def dup(self,nums,start,j):

        for k in range(start+1,j):
            if nums[k] ==  nums[j]:return  True
        return  False

    def swap(self,nums,i,j):
        if i == j:
            return
        a = nums[i]
        nums[i]  = nums[j]
        nums[j] = a

if __name__ == '__main__':

    so = Solution()
    ans = so.permuteUnique([3,3,0,0,2,3,2])
    print(len(ans))
    print(ans)
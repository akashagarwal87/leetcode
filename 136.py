class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        for i in set(nums):
            if nums.count(i) == 1:
                return i
        
s=Solution()
print(s.singleNumber([2,2,1]))
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        lastColor=2
        for j in range(len(nums)):
            if nums[j] == lastColor:
                
s=Solution()
l=[]
print(l)
s.sortColors(l)
print(l)
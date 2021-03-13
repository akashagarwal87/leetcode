class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1 or nums.count(val) <= 0:
            return len(nums)
       
        while nums.count(val) > 0:
            print("here")
            nums.pop(nums.index(val))
        return len(nums)
    def removeDupRec(self,nums):
        lastnumber=-9999999
        
s=Solution()
nums = [3,2]
print(s.removeElement(nums,1))
print(nums)
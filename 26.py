class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            count=0
            while nums.count(i) > 1:
                nums.pop(nums.index(i))
        return len(nums)
    def removeDupRec(self,nums):
        lastnumber=-9999999
        
s=Solution()
nums = [1,1,2]
print(s.removeDuplicates(nums))
print(nums)
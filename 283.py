class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[i] == 0:
                # print(i)
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        
s=Solution()
l=[1,0,1,0,3,12]
print(l)
s.moveZeroes(l)
print(l)
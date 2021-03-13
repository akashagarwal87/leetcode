class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rtype=-1
        try:
            rtype=nums.index(target)
        except Exception as e:
            rtype = -1
        if rtype == -1:
            ## perform binary search
            rtype=len(nums)
            for i in range(len(nums)-1):
                print(i)
                if nums[i] < target and target < nums[i+1]:
                    rtype=i+1
                    break
                elif nums[i] > target:
                    rtype=i
                    break
            if len(nums) == 1 and nums[0] > target:
                rtype = 0
                
        return rtype

s=Solution()
print(s.searchInsert([1],0))
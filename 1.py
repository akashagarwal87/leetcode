class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum=0
        for i in range(len(nums)-1):
            sum=nums[i]
            rtype=[i]
            for j in nums[i+1:]:
                if sum+j == target:
                    print("{}.......{}".format(i,nums[i+1:].index(j)))
                    print("........{}".format(rtype))
                    rtype.append(nums[i+1:].index(j)+i+1)
                    print("......1111111..{}".format(rtype))
                    return rtype

s=Solution()
# s.twoSum([2,7,11,15],9)
s.twoSum([3,2,4],6)
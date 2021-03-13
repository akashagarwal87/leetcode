class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtype=0
        maxcount=0
        for i in set(nums):
            n=nums.count(i)
            if n > maxcount:
                rtype=i
                maxcount=n
        return rtype


s=Solution()
print(s.majorityElement([3,2,2,2,2,3]))
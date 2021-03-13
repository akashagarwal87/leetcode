class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        peak=sorted(arr)[-1]
        return arr.index(peak)

s=Solution()
print(s.peakIndexInMountainArray([3,4,5,1]))
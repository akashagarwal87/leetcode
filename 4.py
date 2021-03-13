class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        zipSorted=nums1+nums2
        zipSorted.sort()
        print(zipSorted)
        if len(zipSorted)%2 == 0:
            return (zipSorted[int(len(zipSorted)/2) -1] + zipSorted[int(len(zipSorted)/2)])/2
        else:
            return zipSorted[int(len(zipSorted)/2)]
        

s=Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1,nums2))
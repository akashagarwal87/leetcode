class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtype=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                rtype.append(nums[i+1])
        return rtype
if __name__ == "__main__":
    h=[1,1,2,3]
    print(Solution().decompressRLElist(h))

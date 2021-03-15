class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        rtype=[None for i in range(len(index))]
        for i in zip(index,nums):
            if rtype[i[0]] == None:
                rtype[i[0]]=i[1]
            else:
                ##shift the array from that postion
                rtype=rtype[:i[0]]+[i[1]]+rtype[i[0]:]
                rtype.pop()
        return rtype

if __name__ == "__main__":
    print(Solution().createTargetArray([1,2,3,4,0],[0,1,2,3,0]))
    print(Solution().createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
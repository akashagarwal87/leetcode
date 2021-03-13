class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        sqrResult=[x*x for x in A]
        sqrResult.sort()
        return sqrResult
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[row[i] for row in A] for i in range(len(A[0]))]
        
s=Solution()
print(s.transpose([[1,2,3],[4,5,6]]))
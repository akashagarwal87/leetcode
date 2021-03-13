class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        rtype=[]
        numofNegative=int(n/2)
        checkEvenOdd=n%2
        for i in range(numofNegative):
            rtype.append(-1*(i+1))
        if checkEvenOdd != 0:
            rtype.append(0)
        for i in range(numofNegative):
            rtype.append((i+1))
        return rtype
        
s=Solution()
print(s.sumZero(6))
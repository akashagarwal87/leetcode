class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype=[]
        for i in range(n):
            s=""
            if (i+1)% 3 == 0:
                s="Fizz"
            if (i+1)% 5 == 0:
                s+="Buzz"
            if len(s) <= 0:
                s=str(i+1)
            rtype.append(s)
        return rtype

s=Solution()
print(s.fizzBuzz(20))
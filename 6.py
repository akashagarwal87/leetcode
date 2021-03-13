class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rtype=""
        k=numRows-1
        if len(s) == 1 or numRows == 1:
            return s
        if len(s) == numRows:
            return s
        for i in range(numRows):
            try:
                print((k*2)+2*i)
                rtype+=s[(k*2)+2*i]
            except Exception as e:
                k-=1
                pass
        return rtype
s=Solution()
print(s.convert("ABCDEF",5))

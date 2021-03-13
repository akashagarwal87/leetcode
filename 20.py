class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo=['(','{','[']
        lc=[')','}',']']
        bl=[]
        rtype=False
        if len(s)%2 != 0:
            return rtype
        count=0
        for i in range(len(s)):
            if s[i] in lo:
                bl.append(s[i])
            else:
                if (i==0 and s[i] in lc) or len(bl) <= 0:
                    return rtype
                if lo[lc.index(s[i])] != bl[-1]:
                    return rtype
                bl.pop()
        if len(bl) > 0:
            return False
        return True
        
s=Solution()
dataSet=['[]]','[][]','([)]','{[]}','((',"(){}}{"]
for data in dataSet:
    print(s.isValid(data))
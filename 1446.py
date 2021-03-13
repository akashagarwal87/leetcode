class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtype=0
        maxcount=0
        lastChar=""
        for i in s:
            if i != lastChar:
                lastChar=i
                if maxcount < rtype:
                    maxcount = rtype
                rtype=1
            else:
                rtype+=1
        if maxcount < rtype: maxcount = rtype
        return (maxcount)
s=Solution()
print(s.maxPower("j"))
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        o=""
        if s[0] == "-":
            o="-"
            s=s[1:]
        # print(s)
        s1=[i for i in s ]
        s1.reverse()
        o+=''.join(s1)
        if  -2147483648 <= int(o) <= 2147483647:
            return int(o)
        else:
            return 0
        
s=Solution()
print(s.reverse(1534236469))
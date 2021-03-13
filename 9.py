class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        s1=[i for i in s ]
        s1.reverse()
        s1=''.join(s1)
        print(s1)
        print(2)
        if s == s1:
            return True
        else:
            return False
        
        
s=Solution()
print(s.isPalindrome(121))
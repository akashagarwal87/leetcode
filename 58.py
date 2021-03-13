class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return len(s.split()[-1])
        print(s)
        print(s.replace(" ",""))
        if(len(s.replace(" ",""))>=1):
            return len(s.split()[-1])
        else:
            return 0

s=Solution()
print(s.lengthOfLastWord("Hello World"))
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sArr=s.split()
        sArrout=[]
        for i in sArr:
            sArrout.append(i[::-1])
        return ' '.join(sArrout)
        
s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))
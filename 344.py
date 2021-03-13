class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()

s=Solution()
l=["h","e","l","l","o"]
print(l)
s.reverseString(l)
print(l)
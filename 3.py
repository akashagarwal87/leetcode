class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength=0
        listOfChar=[]
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if i != len(s) -1:
                if s[i] != s[i+1]:
                    if s[i] not in listOfChar:
                        listOfChar.append(s[i])
                    else:
                        if len(listOfChar) > maxLength:
                            maxLength=len(listOfChar)
                        listOfChar=[]
                        continue
                else:
                    if s[i] not in listOfChar:
                        listOfChar.append(s[i])
                    if len(listOfChar) > maxLength:
                        maxLength=len(listOfChar)
                    listOfChar=[]
                    listOfChar.append(s[i])
            else:
                if s[i] not in listOfChar:
                    listOfChar.append(s[i])
            if len(listOfChar) > maxLength:
                maxLength=len(listOfChar)

        return maxLength
        
s=Solution()
print(s.lengthOfLongestSubstring("dvdf"))
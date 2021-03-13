class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        maxLength=len(arr[0])
        s=""
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                s+=arr[i]+arr[j]
                noOfUniqChar=len(set([x for x in s]))
                if len(s) != (noOfUniqChar):
                    s=""
                if noOfUniqChar > maxLength:
                    maxLength = noOfUniqChar
        return maxLength


s=Solution()
print(s.maxLength(["un","iq","ue"]))
print(s.maxLength(["cha","r","act","ers"]))
print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(s.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))
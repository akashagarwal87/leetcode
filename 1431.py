import datetime

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        rtype=[]
        maxcandies=max(candies)
        for i in candies:
            if (i+extraCandies) >= maxcandies:
                rtype.append(True)
            else:
                rtype.append(False)
        return rtype
if __name__ == "__main__":
    h1=[[2,3,5,1,3],[4,2,1,1,2]]
    extra=[3,1]
    for h in zip(h1,extra):
        print(datetime.datetime.now())
        print(Solution().kidsWithCandies(h[0],h[1]))
        print(datetime.datetime.now())
        print("--"*20)
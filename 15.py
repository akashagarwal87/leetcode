import datetime
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rtype=[]
        if len(nums) < 2:
            return rtype
        nums.sort()
        dupArr=[]
        for i in range(len(nums)-1):
            t=[]
            try:
                # print(0-(nums[i]+nums[i+1]))
                targetIndex=nums.index(0-(nums[i]+nums[i+1]))
                if targetIndex >= 0 and targetIndex != i and targetIndex != (i+1):
                    dup=set()
                    t.append(nums[i])
                    t.append(nums[i+1])
                    t.append(nums[targetIndex])
                    dup.add(nums[i])
                    dup.add(nums[i+1])
                    dup.add(nums[targetIndex])
                    # print(t)
                    # print(dupArr)
                    if dup not in dupArr:
                        rtype.append(t)
                        dupArr.append(dup)
            except ValueError:
                pass

        return rtype

if __name__ == "__main__":
    h1=[[0],[],[-1,0,1,2,-1,-4],[0,0,0],[-1,0,1,0]]
    for h in h1:
        print(datetime.datetime.now())
        print(Solution().threeSum(h))
        print(datetime.datetime.now())
        print("--"*20)
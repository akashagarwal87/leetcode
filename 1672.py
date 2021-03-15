class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rtype=0
        for i in accounts:
            rtype=max(rtype,sum(i))
        return rtype
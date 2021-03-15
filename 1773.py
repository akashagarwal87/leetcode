class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        t=['type','color','name']
        ruleindex=t.index(ruleKey)
        rtype=0
        for i in items:
            if i[ruleindex] == ruleValue:
                rtype +=1
        return rtype
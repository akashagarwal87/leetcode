class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rtype={}
        l1l=self.prepareList(l1)
        l2l=self.prepareList(l2)
        l1l.reverse()
        l2l.reverse()
        rtypes=str(int(''.join([str(x) for x in l1l])) + int(''.join([str(x) for x in l2l])))
        old=None
        for i in range(len(rtypes)):
            if i ==0:
                old=ListNode(rtypes[i])
                continue
            updated=ListNode(rtypes[i],old)
            old=updated
            rtype=updated
        return rtype
    
    def prepareList(self,l):
        l1l=[]
        cur=l
        while cur.next != None:
            l1l.append(cur.val)
            cur=cur.next
        l1l.append(cur.val)
        return l1l
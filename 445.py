# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        val1=self.extractList(l1)
        val2=self.extractList(l2)
        sum=str(int(val1)+int(val2))
        rtype=None
        for x in sum[::-1]:
            rtype=ListNode(int(x),rtype)
    
    def extractList(self,l):
        if l == None: return "0"
        ll=[]
        while l.next != None:
            ll.append(l.val)
            l=l.next
        ll.append(l.val)
        
        return ''.join([str(s) for s in ll])
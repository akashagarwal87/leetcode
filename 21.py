# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2==None:
            return l1
        l1l=self.extractListfromLL(l1)
        l2l=self.extractListfromLL(l2)
        outputList=l1l+l2l
        outputList.sort()
        print(self.prepareLL(outputList))

        
    def extractListfromLL(self,l):
        ll=[]
        if l == None:
            return ll
        while l.next != None:
            ll.append(l.val)
            l=l.next
        ll.append(l.val)
        return ll
    
    def prepareLL(self,l):
        ln=None
        l.reverse()
        for i in range(len(l)):
            if i==0:
                ln=ListNode(val=l[i],next=None)
                continue
            ln=ListNode(val=l[i],next=ln)

        return ln

s=Solution()
l1=ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
l2=ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
print(s.mergeTwoLists(l1,l2))
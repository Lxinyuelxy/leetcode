# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = dummy
        while p1!=None and p2!=None:
            if p1.val <= p2.val:
                p3.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p3.next = ListNode(p2.val)
                p2 = p2.next
            p3 = p3.next
        
        while p1!= None:
            p3.next = ListNode(p1.val)
            p1 = p1.next
            p3 = p3.next
        while p2 != None:
            p3.next = ListNode(p2.val)
            p2 = p2.next
            p3 = p3.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = ListNode()
        orig = dummy
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next 
            
        while l1 and not l2:
            cur.next = l1
            l1 = l1.next 
            cur = cur.next 

        while l2 and not l1:
            cur.next = l2
            l2 = l2.next 
            cur = cur.next 
                
        return orig.next 
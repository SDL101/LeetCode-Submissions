# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head
        slow = head
        
        if head.next is None:
            return None
        
        fast = fast.next.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return head
            
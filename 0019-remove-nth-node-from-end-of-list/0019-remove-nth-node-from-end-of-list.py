# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        slow, fast = curr, curr 
        
        for each in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
        
        slow.next = slow.next.next
    
        return dummy.next
    
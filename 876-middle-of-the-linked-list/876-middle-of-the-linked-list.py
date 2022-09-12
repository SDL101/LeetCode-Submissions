# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next 
        
        while slow and fast:
            slow = slow.next
            if not fast.next:
                fast = fast.next
            else:
                fast = fast.next.next
        return slow
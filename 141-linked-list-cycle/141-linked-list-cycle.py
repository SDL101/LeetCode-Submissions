# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visNodeMap = {}
        
        while head:
            if head.next is None:
                return False
            elif head in visNodeMap:
                return True
            visNodeMap[head] = 0
            head = head.next
        
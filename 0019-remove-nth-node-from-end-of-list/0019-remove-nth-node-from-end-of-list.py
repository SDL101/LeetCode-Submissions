# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy head, dummy head ptr, and 2 ptrs for sliding, start right pointer over n times, then slide both ptrs together until right.next is None. remove by setting left.next = right. return dummy head.next

        # head = [X, 1,  2,  3,  4,  5], n = 2
                            #  ^       ^
        # head = [X, 1], n = 1
            
                #  ^  ^

        dummyHead = ListNode()
        dummyHead.next = head
        l, r = dummyHead, dummyHead
        # position right ptr n positions ahead
        for each in range(n):
            r = r.next
        # slide both ptrs until r reaches last node
        while r.next:
            l = l.next
            r = r.next
        # remove nth node
        l.next = l.next.next
        # return head of list
        return dummyHead.next
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodePtr = head
        nodeValList = []
        
        while nodePtr:
            nodeValList.append(nodePtr.val)
            nodePtr = nodePtr.next
            
        maxPairSum, currPairSum = 0, 0
        length = len(nodeValList)
        
        for i in range(length - 1, -1, -1):
            pairIndex = length - 1 - i
            currPairSum = nodeValList[i] + nodeValList[pairIndex]
            maxPairSum = max(currPairSum, maxPairSum)
            
        return maxPairSum
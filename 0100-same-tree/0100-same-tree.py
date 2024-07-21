# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #both trees were empty or we successfully recursed to the base case - return true
        if not p and not q:
            return True
        
        #found node existence diff - return false
        if not p or not q:
            return False
        
        #found node value diff between trees during recursion - return false
        if p.val != q.val:
            return False
        
        #return the res of calling both left and right recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
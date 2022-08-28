# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #can it be an empty tree? - YES
        #can my nodes contain pos an neg values - YES
        #only ints? - YES
    
        #if p and q are both none return true
        #if p is none and q is not none then return false
        #if p is not none and q is none then return false
        
        #if value of p == q 
        #then visit the left child of each tree and check again
        #once the left child is none, check the right child
        
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif q is not None and p is None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
            
            
            
        
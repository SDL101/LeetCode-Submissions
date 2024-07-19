# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = []
        stack.append((1, root))
        
        depth = 0
        while len(stack) > 0:
            currDepth, root = stack.pop()
            if root is not None:
                depth = max(depth, currDepth)
                stack.append((currDepth + 1, root.left))
                stack.append((currDepth + 1, root.right))
        return depth
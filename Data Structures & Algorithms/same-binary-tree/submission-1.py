# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(p, q, equal):
            if not equal:
                return False
            if p and q:
                equal = p.val == q.val
                if equal:
                    equal = traverse(p.left, q.left, equal)
                    equal = traverse(p.right, q.right, equal)
                return equal
            elif not p and not q:
                return True
            return False

        return traverse(p, q, True)
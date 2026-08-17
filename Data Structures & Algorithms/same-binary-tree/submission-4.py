# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
    
        def traverse(p, q, state):
            if not state:
                return False
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                state = traverse(p.left, q.left, True)
                state = traverse(p.right, q.right, state)
                return state
            else:
                return False
        
        if p and q and p.val == q.val:
            state = traverse(p.left, q.left, True)
            state = traverse(p.right, q.right, state)
            return state
        return False
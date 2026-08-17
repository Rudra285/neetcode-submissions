# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse_subtree(root, subroot, equal):
            if not equal:
                return False
            if root and subroot:
                equal = root.val == subroot.val
                if equal:
                    equal = traverse_subtree(root.left, subroot.left, equal)
                    equal = traverse_subtree(root.right, subroot.right, equal)
                return equal
            elif not root and not subroot:
                return True
            return False
        
        def traverse(root, subroot, found):
            if root and not found:
                found = root.val == subroot.val
                if found:
                    found = traverse_subtree(root, subroot, True)
                if not found:
                    found = traverse(root.left, subroot, found)
                    found = traverse(root.right, subroot, found)
            return found
        
        return traverse(root, subRoot, False)


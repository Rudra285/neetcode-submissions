# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def traverse(left_node, right_node):
            if left_node or right_node:
                if left_node:
                    left_node.left, left_node.right = left_node.right, left_node.left
                if right_node:
                    right_node.left, right_node.right = right_node.right, right_node.left
                if left_node and right_node:
                    traverse(left_node.left, right_node.right)
                    traverse(left_node.right, right_node.left)
                elif not left_node:
                    traverse(right_node.left, right_node.right)
                else:
                    traverse(left_node.left, left_node.right)


        root.left, root.right = root.right, root.left
        # traverse(root.left, root.right)
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
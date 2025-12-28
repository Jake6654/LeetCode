# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I use a recursive DFS
The key idea is that we keep going left until there's no left child.
And when a node has no left child, it is the moment we record its value
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder traversal: left -> root -> right
        res = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

from idlelib.tree import TreeNode
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    class Solution:
        def diameterOfBinaryTree(self, root:Optional[TreeNode]):

            diameter = 0

            def dfs(node: Optional[TreeNode]) -> int:

                nonlocal diameter

                left_depth = dfs(node.left)
                right_depth = dfs(node.right)

                # Updates diameter at each node
                # Since each node could be the midpoint of the longest path
                diameter = max(diameter, left_depth + right_depth)

                return max(left_depth, right_depth) + 1

            dfs(root)
            return diameter

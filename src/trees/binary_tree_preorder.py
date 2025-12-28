# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
What confused me while solving this problem was that when a node has no children,
the recursion tracksback to its parent. I initially thought when the code revisits
 the parent, it adds the parent to the list again. However, after thinking about it more,
I realized that recursion simply returns to the parent call, not running the same code again.
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # create a list to track visit nodes preorder
        l = []

        def dfs(node:Optional[TreeNode]):
            if not node:
                return

            l.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return l
from idlelib.tree import TreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    class Solution:
        def isBalanced(self, root: TreeNode) -> bool:

            def dfs(node):

                if not node:
                    return True

                left = dfs(node.left)
                # if the height's diff is already over 1
                # immediately return -1
                if left == -1:
                    return -1

                right = dfs(node.left)
                if right == -1:
                    return -1

                if abs(left - right) > 1:
                    return -1

                return  1 + max(left, right)
            return dfs(root) != -1
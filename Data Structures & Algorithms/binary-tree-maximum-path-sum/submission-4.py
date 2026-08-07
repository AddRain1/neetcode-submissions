# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxSum = float("-inf")

        def dfs(curr):
            if not curr:
                return 0

            left = max(0, dfs(curr.left))
            right = max(0, dfs(curr.right))

            self.maxSum = max(self.maxSum, curr.val + left + right)

            # dfs returns max of sum path
            return curr.val + max(left, right)

        dfs(root)

        return self.maxSum
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    counter = 0 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_distance = 0

        def dbt(root):
            nonlocal max_distance
            if not root:
                return 0
            left = dbt(root.left)
            right = dbt(root.right)

            max_distance = max(max_distance,left + right)
            return 1 + (max(left,right))

        dbt(root)
        return max_distance
        

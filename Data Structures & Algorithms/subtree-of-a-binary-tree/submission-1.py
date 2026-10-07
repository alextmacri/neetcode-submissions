# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def bracket_encode_tree(node: Optional[TreeNode]) -> str:
            # Base case: node is None
            if not node:
                return ''
                
            # Use brackets to recursively denote nodes, seperated by commas
            return '(' + str(node.val) + bracket_encode_tree(node.left) + bracket_encode_tree(node.right) + ')'
        
        # Encode the trees and compare
        return bracket_encode_tree(subRoot) in bracket_encode_tree(root)
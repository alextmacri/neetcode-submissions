# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # We can check for equality starting at every subtree of the root
        #   with the subroot, but that would be O(m * n) for time and space
        #   with recursion and DFS. We can do better by encoding the tree in
        #   a way that lets us just go through each once, and then linearly
        #   compare them to check if the subroot's tree appears in the root's
        #   tree. This means we need to encode the tree in a way that matches
        #   the RECURSIVE pattern-matching that we would get with DFS. We can
        #   see that the BFS-adjacent encoding they use for the function input
        #   wouldn't work for this, so how about we try a DFS-adjacent one?

        def bracket_encode_tree(node: Optional[TreeNode]) -> str:
            # Base case: node is None
            if not node:
                return ''
                
            # Use brackets to recursively denote nodes, seperated by commas
            return '(' + str(node.val) + bracket_encode_tree(node.left) + bracket_encode_tree(node.right) + ')'
        
        # Encode the trees and compare
        return bracket_encode_tree(subRoot) in bracket_encode_tree(root)
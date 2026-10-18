# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def _check_direction_same(node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
            """
            Helper function to see if nodes "go in the same direction".
            """
            return (node.val < p.val) == (node.val < q.val)

        curr_node = root

        while curr_node and curr_node != p and curr_node != q and _check_direction_same(curr_node, p, q):
            # Current node isn't one of the child nodes and they both go in
            #   the same direction => traverse in that direction
            if curr_node.val > p.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        return curr_node
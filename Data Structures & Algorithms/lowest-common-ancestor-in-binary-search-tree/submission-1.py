# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        All values are unique, so we can compare nodes on equality by looking
        at their values (actually, I think Python/the TreeNode class handles
        the equality for us). Also, since it's a BST, we know what direction
        they both are relative to the current node (left child if less than,
        right child if greater than). This means that we can go down from the
        root and know exactly when they diverge, and take that as the lowest
        common ancestor (since in the next layer of traversal, they will no
        longer be at a common ancestor, and there's no way in a BST to
        converge again). Since p != q and p and q are both guarunteed to be in
        the tree, there aren't really any edge cases to worry about (though as
        always, we may find some once we start testing). One thing that can
        happen according to the constraints is that the root itself is one of
        the nodes in question, but since a node can be a descendant of itself,
        we would just put the root as the LCA for that.
        """
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
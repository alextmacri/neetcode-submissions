# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive data structure where we're traversing and trying to find a
        #   property of, BUT the property doesn't require numerical info to be
        #   passed up the tree recursively to efficiently compute, and the
        #   "internal reasoning" can be done with the return format of the
        #   final return, so we don't need a helper function and global var.
        #   Traverse with DFS since height for average/balanced binary tree is
        #   log2(n), while width is n/2, so it's quicker to find them further
        #   down

        # DFS will process/return before recursing since it's sort of an
        #   "early-return" situation where we just need them to be inequal at
        #   some point and don't need values from further in the traversal
        #   to get the current value. Verify that a path to leaf node is equal
        #   once you get to the bottom without disqualifying early by
        #   returning False

        # Base case: both p and q are None (bottom has been reached)
        if not p and not q:
            return True
        
        # Check for same structure (one of p or q (not both) are None)
        if not p or not q:
            return False
        
        # Check for same values
        if p.val != q.val:
            return False
        
        # Traverse deeper, it has children but may still be equal
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
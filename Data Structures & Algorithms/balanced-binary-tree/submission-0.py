# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive data structure so we will have to recursively iterate
        #   through it, but while traversing we care about the max heights,
        #   but for the final return we need a bool, so we need a recursive
        #   helper that checks the height along the way (global variable), but
        #   returns the max height (the only thing that matters for balancing)
        #   so we can continue to compare as we continue "up" the tree (DFS)
        is_balanced = True
        
        def height_check_balance(node: Optional[TreeNode]) -> int:
            # Base case: node is None (parent is leaf)
            if not node:
                return 0
            
            # Fuckass Python scoping
            nonlocal is_balanced
            
            # Recurse (DFS, so "go all the way down" before doing stuff)
            # NOTE: don't add 1 to these, since the base case is that the
            #   parent is a leaf, so the 1 for height will get added once the
            #   parent's pass through the traversal is done
            left_height = height_check_balance(node.left)
            right_height = height_check_balance(node.right)
            
            # Check balance
            if abs(left_height - right_height) > 1:
                is_balanced = False

            # Return max height
            return max(left_height, right_height) + 1
        
        # DON'T FORGET TO CALL THE FUNCTION MORON
        height_check_balance(root)

        return is_balanced
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive data structure, so we need to recursively get our stuff
        #   then compute, but this time the final value may not go through the
        #   root (which is where the bottom of the recursive stack is, and
        #   thus where the final return needs to come from). Since each node's
        #   value can be "independant" from each other, we need to keep track
        #   of this outside of the algorithm/return values itself, and the
        #   easiest way to do that is with a global variable (using a helper
        #   function as well so we can make the right choice at the end)
        max_middle_path = 0

        def max_height_and_path(node: Optional[TreeNode]) -> int:
            # Base case: root is None
            if not node:
                return 0
            
            nonlocal max_middle_path

            # Since it's a binary tree, the 3 kinds of ways to get a diameter are
            #   traversing down from the left side to the parent, traversing down
            #   from the right side to the parent, and going through the current
            #   node from the left side to the right side. But, for each of these,
            #   only the largest path down from the left and right sides matter to
            #   compute the above nodes, and we only care about the path through
            #   middle if it's the new largest (independant, hence the global
            #   variable)
            left_height = max_height_and_path(node.left)
            right_height = max_height_and_path(node.right)

            middle_path = left_height + right_height
            if middle_path > max_middle_path:
                max_middle_path = middle_path
            
            return max(left_height, right_height) + 1
        
        max_height_and_path(root)
        return max_middle_path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Edge case: root is None
        if not root:
            return None

        # Tree is a recursive data structure, so for basic structural changes
        #   like this, we will need to do it with recursion. When making
        #   structural changes like this where you need to "see the tree as
        #   it is first" (which isn't fully the case here, but I'd like to
        #   make an example of it), then the strategy is to recursively
        #   traverse first, then make the changes

        # No need to check if it's null, we get that in the Edge case check
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Implicit base case & what has to be done after recursive step
        #   anyway, swap children (fine even if it's None), and return it
        root.left, root.right = root.right, root.left

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: root is None
        if not root:
            return 0

        # As usual for recursive data structure algorithms, we'll need to
        #   recurse further then do the "actual work", using what we get from
        #   recursing further. Not going to do a mathematical proof, but it
        #   follows that only the max depth path from a child could contribute
        #   to a max depth path to a parent (not the other, smaller path), so
        #   we can "discard" the other path length by not returning it. This
        #   also makes it convenient for us since that's the exact format the
        #   full algorithm return is, so we don't need to make a helper func
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
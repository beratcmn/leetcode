# Runtime 60 ms Beats 6.56%
# Memory 16.3 MB Beats 22.59%

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        elif left and right:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return False
    
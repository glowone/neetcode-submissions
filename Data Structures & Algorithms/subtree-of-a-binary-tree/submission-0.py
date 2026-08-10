class Solution: 
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool: 
        if not t: return True
        if not s: return False

        if self.sameTree(s,t):
            return True

        return (self.isSubtree(s.left, t) or 
                self.isSubtree(s.right, t))

    def sameTree(self, s, t): 
        if not s and not t: 
            return True
        if not s or not t or s.val != t.val:
            return False 

        return (self.sameTree(s.right, t.right) and self.sameTree(s.left, t.left))

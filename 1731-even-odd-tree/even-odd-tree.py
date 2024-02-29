class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def helper(indicator,root ):
           
            if not root:
                return True
            level = []
            for elem in root:
                
                if elem.left:
                    level.append(elem.left)
                if elem.right:
                    level.append(elem.right)
        
            if indicator: 
                for i,elem in enumerate(level):
                    if elem.val % 2 ==0:
                        return False
                    if i >= 1:
                        if elem.val <= level[i -1].val:
                            return False
                indicator = False
            else:
                for i,elem in enumerate(level):
                    if elem.val % 2 == 1:
                        return False
                    if i>= 1:
                        if elem.val >= level[i -1].val:
                            return False
                indicator = True
            return helper(indicator, level)
        if root.val % 2 == 0:
            return False
        return helper(False, [root])


                        
                    

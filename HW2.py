# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        res = [0] 
        self.dfs(root, L, R, res) 
        return res[0] 
    
    def dfs(self, root, L, R, res): 
        if not root: 
            return 
        if L <= root.val <= R: 
            res[0] += root.val 
        if root.val < R: 
            self.dfs(root.right, L, R, res) 
        if root.val > L: 
            self.dfs(root.left, L, R, res)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        res = []      
        
        q = deque()
        q.append(root)
        
        while len(q) != 0:
            notFound = True
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                if node == None: continue
                    
                q.append(node.right)
                q.append(node.left)
                
                if notFound:
                    res.append(node.val)
                    notFound = False
                    
        return res
            
        
from queue import Queue

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    # Write your code here.
    if root is None:
        return []
    q = Queue(0)
    q.put(root)
    res = []
    while q.empty() == False:
        remNode = q.get()
        res.append(remNode)
        
        if remNode.left is not None:
            q.put(remNode.left)
        
        if remNode.right is not None:
            q.put(remNode.right)
    ans = [0]*(len(res))        
    if q.empty() == True:
        j = 0
        for i in range(len(res)-1,-1,-1):
            ans[j]=res[i].val
            j += 1
    return ans    
  

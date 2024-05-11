from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    import ipdb
    ipdb.set_trace()
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result

# 示例使用
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(1)
root3 = None

print(levelOrder(root1))  # 输出: [[3],[9,20],[15,7]]
print(levelOrder(root2))  # 输出: [[1]]
print(levelOrder(root3))  # 输出: []


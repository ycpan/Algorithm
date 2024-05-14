class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    import ipdb
    ipdb.set_trace()
    if not root or root == p or root == q:
        # 这个地方是先检索是不是到达空节点了，或者已经到达p和q的位置了，如果是，则不再递归，开始向上新的路径。
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:# left和right不为空，说明，已经找到了p或者q了(否则遍历结束的条件应当为空节点返回）
        # 这个地方是，p和q已经都找到了，也就是说，当前的root通过递归left和right，可以找到p和q，同时，这个又是递归程序，此处的root就是离left和right最近的root
        return root
    return left if left else right
# 示例使用：
# 构建二叉树
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
p = root.left
q = root.left.right.right
print(lowestCommonAncestor(root, p, q).val)  # 输出应该是 5

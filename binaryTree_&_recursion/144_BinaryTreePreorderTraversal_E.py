# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 用遍历的思路计算前序遍历结果
class Solution:
    def __init__(self):
        self.res = []
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.traverse(root)
        return self.res

    # 二叉树遍历函数
    def traverse(self, root: TreeNode):
        if root is None:
            return
        # 前序位置
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

# 分解问题的思路
class Solution:
    # 定义：输入一棵二叉树的根节点，返回这棵树的前序遍历结果
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        # 前序遍历的结果，root.val 在第一个
        res.append(root.val)
        # 利用函数定义，后面接着左子树的前序遍历结果
        res.extend(self.preorderTraversal(root.left))
        # 利用函数定义，最后接着右子树的前序遍历结果
        res.extend(self.preorderTraversal(root.right)) 
        return res
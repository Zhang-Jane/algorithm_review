from typing import List

def build_tree():
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    g = TreeNode("G")

    e.left = a
    e.right = g
    a.right = c
    c.left = b
    c.right = d
    g.right = f

    root = e
    return root
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        stack = []
        ans = []

        stack.append(root)

        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)  # 先把右侧压进去，左侧的才能先pop出来
            if node.left:
                stack.append(node.left)

        return ans

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        stack = []
        ans = []

        while stack or root:  # or root 用来处理根节点
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()  # 到底了，回到上一层
            ans.append(root.val)  # 中序遍历，访问中间节点
            root = root.right  # 转向右子树

        return ans

    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        stack = []
        ans = []

        while stack or root:  # or root 用来处理根节点
            while root:
                stack.append(root)
                ans.insert(0, root.val)  # 整个结果的倒置，后面来的插入到前面去
                root = root.right  # 先转向右边了
            root = stack.pop()  # 到底了，回到上一层
            root = root.left  # 再转向左边

        return ans

root = build_tree()
s = Solution()

result1 = s.preorderTraversal(root)
result2 = s.inorderTraversal(root)
result3 = s.postorderTraversal(root)
print(result1)
print(result2)
print(result3)
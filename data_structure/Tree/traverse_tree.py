# Definition for a binary tree node.
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
        """
        前序遍历
        :param root:
        :return:
        """
        ans = []

        def preRecursive(root):
            if root is None:
                return
            ans.append(root.val)
            preRecursive(root.left)
            preRecursive(root.right)
        preRecursive(root)

        return ans

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        中序遍历
        :param root:
        :return:
        """
        ans = []

        def inRecursive(root):
            if root is None:
                return
            inRecursive(root.left)
            ans.append(root.val)
            inRecursive(root.right)

        inRecursive(root)

        return ans

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后序遍历
        :param root:
        :return:
        """
        ans = []

        def postRecursive(root):
            if root is None:
                return
            postRecursive(root.left)
            postRecursive(root.right)
            ans.append(root.val)

        postRecursive(root)

        return ans


root = build_tree()
s = Solution()

result1 = s.preorderTraversal(root)
result2 = s.inorderTraversal(root)
result3 = s.postorderTraversal(root)
print(result1)
print(result2)
print(result3)
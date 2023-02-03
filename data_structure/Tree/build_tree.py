class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def construct(self, li: list = None):
        """
        构建二叉树：https://blog.csdn.net/baoxin1100/article/details/108025393
        """
        if not li:
            return None
        if len(li) == 0:
            return None
        que = []  # 定义队列
        fill_left = True  # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
        for val in li:
            node = Node(val) if val is not None else None  # 非空值返回节点类，否则返回 None
            if len(que) == 0:
                root = node  # 队列为空的话，用 root 记录根结点，用来返回
                que.append(node)
            elif fill_left:
                que[0].left = node
                fill_left = False  # 填充过左儿子后，改变记号状态
                if node:  # 非 None 值才进入队列
                    que.append(node)
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0)  # 填充完右儿子，弹出节点
                fill_left = True
        return root


# 定义一个dfs打印中序遍历
def dfs(node):
    if node is not None:
        dfs(node.left)
        print(node.val, end=' ')
        dfs(node.right)


# 定义一个bfs打印层序遍历
def bfs(node):
    que = []
    que.append(node)
    while que:
        l = len(que)
        for _ in range(l):
            tmp = que.pop(0)
            print(tmp.val, end=' ')
            if tmp.left:
                que.append(tmp.left)
            if tmp.right:
                que.append(tmp.right)
        print('|', end=' ')


def max_depth(root: Node):
    if root is None:
        return 0
    # print(f"1=={root.val}==1")
    left_max = max_depth(root.left)
    # print(f"2=={root.val}==2")
    right_max = max_depth(root.right)
    # print(f"3=={root.val}==3")
    return 1 + max(left_max, right_max)


if __name__ == "__main__":
    tree_list = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    root = tree.construct(tree_list)
    max_depth(root)

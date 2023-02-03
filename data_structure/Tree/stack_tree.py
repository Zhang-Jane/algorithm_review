from data_structure.Tree.build_tree import Node, Tree


class Stack(object):
    """栈"""

    def __init__(self, init_list=None):
        """创建一个新的空栈"""
        if not init_list:
            self.__list = list()  # 栈底层使用list来实现
        else:
            self.__list = init_list

    @property
    def is_empty(self):
        """判空"""
        return self.__list == []

    def size(self):
        """返回栈中元素个数"""
        return len(self.__list)

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.is_empty:
            return None
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty:
            return None
        return self.__list[self.size() - 1]

    def __repr__(self):
        return str([p.vaule for p in self.__list])


def push_left_branch(p: Node):
    while p is not None:
        # 前序遍历位置，访问左子树，直到叶子节点
        # print(p.vaule)
        stack.push(p)
        p = p.left


def traverse(root: Node):
    push_left_branch(root)
    # 标记上一次遍历完的子树的根节点
    visited: Node = Node(-1)
    while not stack.is_empty:
        p: Node = stack.peek()
        # print(p.vaule)
        # 判断p的坐姿书被遍历完，右子树还没有被遍历的时候:
        if (p.left is None or p.left == visited) and p.right != visited:
            # 中序遍历的位置，当左子树遍历完返回遍历右子树的时候
            push_left_branch(p.right)
        if p.right is None or p.right == visited:
            # 后续遍历的位置，当所有的子树遍历完毕之后，出栈
            visited = stack.pop()
            print(visited.value)


if __name__ == '__main__':
    tree_list = [3, 9, 20, None, None, 15, 7]
    tree = Tree()
    root = tree.construct(tree_list)
    stack = Stack()
    traverse(root)

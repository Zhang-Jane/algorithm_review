from data_structure.Tree.build_tree import Node


class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = list()  # 使用list实现队列

    @property
    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def enqueue(self, item):
        """往队列中添加一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头中取出元素"""
        if self.is_empty():
            return None
        return self.__list.pop(0)


class LevelOrder:
    def __init__(self):
        self.queue = Queue()

    def traverse(self, root: Node):
        self.queue.enqueue(root)
        # 控制层级的遍历
        while not self.queue.is_empty:
            # 当前层的节点数
            q_size = self.queue.size()
            i = 0
            # 控制每一层的节点
            while i < q_size:
                curr_node: Node = self.queue.dequeue()
                if curr_node.left is not None:
                    self.queue.enqueue(curr_node.left)
                if curr_node.right is not None:
                    self.queue.enqueue(curr_node.right)
                i += 1

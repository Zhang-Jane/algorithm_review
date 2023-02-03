class Node:
    """
    节点
    data: 保存数据
    _next: 保存下一个节点的指针
    """
    def __init__(self, data, next=None):
        self.data = data
        self._next = next

    def __repr__(self):
        return str(self.data)

class SingleLink:
    def __init__(self):
        self._head = None  # 定义头结点
        self.length = 0  # 记录链表的长度

    @property
    def is_empty(self) -> bool:
        return self.length == 0

    def append(self, node: Node):
        """
        在链表的末尾添加一个节点
        :param node:
        :return:
        """
        if not self._head:
            self._head = Node
            self.length += 1
        else:
            head_node = self._head
            # 从头节点遍历，一直遍历到尾节点
            while not head_node._next:
                head_node = head_node.next
            # 尾节点连接新插入的节点
            head_node.next = node
            self.length += 1

    def delete(self, index):
        if self.is_empty:
            raise Exception("link table is empty!")
        if index < 0 or index > self.length - 1:
            raise Exception("out of index")
        # 记录节点的index
        j = 0
        prev_node = self._head
        current_node = self._head
        last_node_index = self.length - 1
        # 如果删除的是头结点，头节点的next变成head节点
        if index == 0:
            self._head = current_node._next
            self.length -= 1
        elif index == last_node_index:
            # 如果删除的是最后一个节点，也很简单的，就是把倒数第二个节点next指向None
            while current_node._next and j < last_node_index - 1:
                current_node = current_node._next
                j += 1
            current_node._next = None
        else:
            while current_node._next and j < index:
                prev_node = current_node
                current_node = current_node._next
                j += 1

            prev_node._next = current_node._next
            self.length -= 1
                
            


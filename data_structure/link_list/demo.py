
class Node(object):
    """节点"""

    def __init__(self, value):
        self.value = value
        self.next = None  # 指向下一节点


class LinkList:
    def __init__(self, head: Node = None):
        self.__head = head

    def create_link_list(self, li: list):
        tail = self.__head
        for value in li[1:]:
            node = Node(value)
            tail.next = node
            tail = node

    def traverse(self):
        while self.__head:
            print(self.__head.value)
            self.__head = self.__head.next

    def reverse(self):
        tail = None
        head = self.__head
        while head:
            tmp = head.next
            head.next = tail
            tail = head
            head = tmp
        print(tail)
        self.__head = tail

    def add_last(self, node: Node, val: int):
        if node.next is None:
            return Node(val)
        node.next = self.add_last(node.next, val)
        print(node.value)
        return node

    def remove_last(self, node: Node):
        if node.next is None:
            return None
        # node.value += 1
        node.next = self.remove_last(node.next)

        return node


if __name__ == '__main__':
    li = [2, 4, 5, 6, 8, None]
    head = Node(li[0])
    l = LinkList(head)
    l.create_link_list(li)
    # res = l.add_last(head, 100)
    res = l.remove_last(head)
    # l.reverse()
    l.traverse()

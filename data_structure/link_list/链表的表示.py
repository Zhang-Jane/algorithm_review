class Node(object):
    """
    单链表的节点定义
    """
    def __init__(self, item):
        self.item = item
        self.next = None

#
# head1 = Node(None)
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# print(a.next.item)
#
#
# class DNode(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.pre = None
#         self.next = None

# head2 = DNode(None)
# a = DNode(1)
# b = DNode(2)
# c = DNode(3)
# a.pre = b
# a.next = c
# print(a.pre.item)


class LinkList(object):
    def __init__(self):
        self.head = Node(None)

    # 判断链表是否为空
    def IsEmpty(self):
        p = self.head # 头指针

        if p.next == None:
            print("List is Empty")
            return True
        return False

    # 打印链表
    def PrintList(self):
        if self.IsEmpty():
            return False

        p = self.head
        while p:
            print(p.data,end=' ')
            p = p.next
class Node(object):
    """
    单链表的节点定义
    """

    def __init__(self, item):
        self.item = item
        self.next = None


# 头部插入元素
def insertFront(self, val):
    node = ListNode(val)
    node.next = self.head
    self.head = node


# 尾部插入元素
def insertRear(self, val):
    node = ListNode(val)
    cur = self.head
    while cur.next:
        cur = cur.next
    cur.next = node


# 中间插入元素
def insertInside(self, index, val):
    count = 0
    cur = self.head
    while cur and count < index - 1:
        count += 1
        cur = cur.next

    if not cur:
        return 'Error'

    node = ListNode(val)
    node.next = cur.next
    cur.next = node


# 改变元素
def change(self, index, val):
    count = 0
    cur = self.head
    while cur and count < index:
        count += 1
        cur = cur.next

    if not cur:
        return 'Error'

    cur.val = val


# 链表头部删除元素
def removeFront(self):
    if self.head:
        self.head = self.head.next


# 链表尾部删除元素
def removeRear(self):
    if not self.head.next:
        return 'Error'

    cur = self.head
    while cur.next.next:
        cur = cur.next
    cur.next = None


# 链表中间删除元素
def removeInside(self, index):
    count = 0
    cur = self.head

    while cur.next and count < index - 1:
        count += 1
        cur = cur.next

    if not cur:
        return 'Error'

    del_node = cur.next
    cur.next = del_node.next


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
        p = self.head  # 头指针

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
            print(p.data, end=' ')
            p = p.next

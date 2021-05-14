class Node(object):
    """
    单链表的节点定义
    """

    def __init__(self, item):
        self.item = item  # 表示数据元素
        self.next = None  # 表示指针


class SingleLinkList(object):
    """
    头结点记录链表的长度,
    """
    def __init__(self, li, method="tail"):
        if method == "head":
            self.create_link_head(li)
        elif method == "tail":
            self.create_link_tail(li)

    def create_link_head(self, li):
        """
        从头插入数据，所以输出的顺序是逆序的。
        头插法的思路：从头节点开始让每一个元素的next指针，指向当前的节点
        插入的过程如下：
        A:[data][next]
                        \

        head:[data][next] -> A:[data][next]

        :param li:
        :return:
        """
        self.head = Node(0)
        for item in li:
            n = Node(item)
            n.next = self.head.next
            self.head.next = n
            self.head.item += 1

    def create_link_tail(self, li):
        """
        从尾部插入数据，所以输出的顺序是正序的。
        尾插法的思路：定义一个尾节点（这个尾结点等于头结点），让尾节点的指针指向每一个元素，然后更新这个尾节点为当前的节点
        head:[data][next] -> A:[data][next]
        :param li:
        :return:
        """
        self.head = Node(0)
        self.tail = self.head
        for item in li:
            p = Node(item)
            self.tail.next = p
            self.tail = p
            self.head.item += 1

    def insert(self, curr_node, insert_node):
        """
        单链表的插入
        :param curr_node: 要插入的当前节点
        :param insert_node: 插入的节点
        :return:
        """
        insert_node.next = curr_node.next
        curr_node.next = insert_node

    def remove(self, curr_node):
        rm_node = curr_node.next
        curr_node.next = curr_node.next.next

    def travel_linklist(self):
        """
        遍历单链表
        :return:
        """
        p = self.head.next
        while p:
            data = p.item
            print(data)
            p = p.next

    def __len__(self):
        return self.head.item


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5]
    s = SingleLinkList(li)
    s.travel_linklist()


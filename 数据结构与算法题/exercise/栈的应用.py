class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top == None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def is_empty(self):
        if self.top == None:
            return True
        return False

    def first(self):
        if self.top == None:
            return None

        return self.top.data

    def __str__(self):
        temp = self.top
        res = ''
        while temp:
            res += temp.data
            temp = temp.next
        return res[::-1]






def infix2postfix(expression):
    output = []
    op_stack = LinkedStack()
    op_priority = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0, ')': 0}

    for e in expression:
        if e == '(':
            op_stack.push(e)
        elif e == ')':
            while op_stack.first() != '(':
                output.append(op_stack.pop())
            op_stack.pop()
        elif e.isdigit():
            output.append(e)
        else:
            while not op_stack.is_empty() and op_priority[op_stack.first()] >= op_priority[e]:
                output.append(op_stack.pop())
            op_stack.push(e)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return ''.join(output)
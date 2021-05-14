"""
给定一个二维矩阵代表一个迷宫，迷宫里面有通道，也有墙壁，通道由数字 0 表示，而墙壁由 1 表示，有墙壁的地方不能通过，那么，能不能从 A 点走到 B 点
"""
maze = [

    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],

]
dirs = [
    lambda x, y: (x-1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x+1, y),
    lambda x, y: (x, y-1),
]


def solve_maze(x1, y1, x2, y2):
    """
    :param x1: 起点的x坐标
    :param y1: 起点的y坐标
    :param x2: 终点的x坐标
    :param y2: 终点的y坐标
    :return:
    """
    stack = []
    stack.append((x1, y1))
    maze[x1][y1] = 2
    while len(stack) > 0:
        current_node = stack[-1]
        if current_node == (x2, y2):
            print("ok")
            print(stack)
            return True
        for d in dirs:
            next_node = d(*current_node)
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            stack.pop()
    else:
        print("没有路")
    return False

solve_maze(1, 1, 5, 3)
# [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (4, 3), (5, 3)]

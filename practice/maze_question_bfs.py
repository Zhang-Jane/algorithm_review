"""
给定一个二维矩阵代表一个迷宫，迷宫里面有通道，也有墙壁，通道由数字 0 表示，而墙壁由 1 表示，有墙壁的地方不能通过，那么，能不能从 A 点走到 B 点
"""
from collections import deque

maze = [

    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
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
    q = deque()
    traceback = []
    q.append((x1, y1, -1))
    maze[x1][y1] = 2
    while len(q) > 0:
        current_node = q.popleft()
        traceback.append(current_node)
        if current_node[:-1] == (x2, y2):
            # for i, v in enumerate(traceback):
            #     print(i, v)
            path = []
            i = len(traceback) - 1
            while i >= 0:
                path.append(traceback[i][:2])
                i = traceback[i][2]
            path.reverse()
            print(path)
            return
        for d in dirs:
            next_node_x,  next_node_y = d(*current_node[:-1])
            # next_node_x,  next_node_y = d(current_node[0], current_node[1])
            if maze[next_node_x][next_node_y] == 0:
                q.append((next_node_x,  next_node_y, len(traceback)-1))
                maze[next_node_x][next_node_y] = 2
    else:
        print("没有路")

solve_maze(1, 1, 5, 3)


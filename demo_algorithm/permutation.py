"""
问题：输入列表L（不含重复元素），输出L的全排列。

如输入：L=[1,2,3]

则输出：[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
import copy


def permutation_nums(li: list, path: list):
    # 触发结束条件，如果满足条件就结束
    if len(path) == len(li):
        c = copy.copy(path)  # 注意这里不是直接将path加到res中，而是浅拷贝了一个对象
        res.append(c)
        return

    for i in li:
        # 排除不合法的选择
        if i in path:
            continue
        else:
            # 做选择
            path.append(i)
            permutation_nums(li, path)
            # 取消选择
            path.pop()


def subset(li: list, start_index: int, path: list):
    c = copy.copy(path)
    res2.append(c)
    for i in range(start_index, len(li)):
        path.append(li[i])
        # 控制树枝，保证不重复
        subset(li, i + 1, path)
        path.pop()


def combine(start_index: int, n: int, k: int, path: list):
    # 触发结束条件，如果满足条件就结束
    if len(path) == k:
        c = copy.copy(path)  # 注意这里不是直接将path加到res中，而是浅拷贝了一个对象
        res.append(c)
        return

    for i in range(start_index, n + 1):
        path.append(i)
        # 控制树枝，保证不重复
        combine(i + 1, n, k, path)
        path.pop()


if __name__ == '__main__':
    res = []
    res2 = []
    L = [1, 2, 3]
    # permutation_nums(L, [])
    combine(1, 4, 2, [])
    print(res)

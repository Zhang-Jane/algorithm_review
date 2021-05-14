def greedy():
    n = 100
    k = 5
    d = [50, 80, 39, 60, 40, 32]
    # 表示加油站之间的距离
    num = 0
    # 表示加油次数
    for i in range(k):
        if d[i] > n:
            print('no solution')
            # 如果得到的任何一个数值大于n，则无法计算
            return

    i, s = 0, 0
    # 利用s进行迭代
    while i <= k:
        s += d[i]
        if s >= n:
            # 当局部和大于n时，将则局部和更新为当前距离
            s = d[i]
            # 贪心意在让每一次加满油之后跑尽可能远的距离
            num += 1
        i += 1
    print(num)


if __name__ == '__main__':
    greedy()
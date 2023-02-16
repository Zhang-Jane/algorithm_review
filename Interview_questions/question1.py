"""
需求1:
平均分配之后，求最大值，平均分配
输入：
5 * 12 = 60
输出：
战斗力高的战队
思考：
最优解
"""
ball = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
}
li = [10, 7, 5, 4]

def get_max_ability(li):
    """
    获取能力最大的组
    :param li:
    :return:
    """
    max_index = 0
    for i in range(1, len(li)):
        if li[i] > li[max_index]:
            max_index = i
    return max_index

times = 60

# 根据时间迭代
while times:
    max_index = get_max_ability(li)
    for i in range(len(li)):
        if i != max_index:
            li[i] += 1
    print(ball[max_index])
    li[max_index] -= 3
    print(li)
    times -= 1

# 时间复杂度O(len(li))=O(n)


"""
需求2:
init_rabbit = 2, per_four_month += 2
输入：10 输出：兔子数量
如果是per_five_month += 2
输入：24 输出：兔子数量
以此类推
提示：
类和数组，⾮斐波那契数列⽅式
思考：
求通用的算法

思路整理：
init_rabbit = 2，after_four_month(times=1) = init_rabbit(2) + init_new_rabbit(2) = 2 * 2
after_four_month(times=2) = rabbit1(2) + rabbit2(2) + rabbit1_new_rabbit(2) + rabbit2_new_rabbit(2) = 2 * 4
"""

def generate_rabbits(times):
    """
    兔子繁殖
    :param times:
    :return:
    """
    if times == 1:
        return 2
    return 2 * generate_rabbits(times - 1)

def get_rabbits(month, interval_month):
    times = month // interval_month
    if times <= 0:
        return 1
    rabbits = generate_rabbits(times)
    return rabbits

print(get_rabbits(10, 4))


"""
需求3:
a = [4,6,3,8...]
将B按照给定数组A相邻数字⼤⼩关系进⾏排列
输入：random_b_length = len(a)
输出：
从所有符合排列的数组中筛选相邻差的绝对值之和最⼤的那些数组
思路：
1. 排列b数组的所有形式
2. 计算max(abs(数组B[j]-B[j-1]))
3. 选出相邻差的绝对值之和最⼤的那些数组
"""


import random
class Solution:
    def __init__(self):
        self.a = [4, 6, 3, 8]
        self.list_len = len(self.a)
        self.b = list(range(len(self.a)))
        random.shuffle(self.b)
        self.max_sum = 0
        self.max_sum_index = 0

    def cal_max(self, list_b):
        """
        相邻差的绝对值之和最⼤
        :param list_b:
        :return:
        """
        sum = 0
        for j in range(1, self.list_len, -1):
            diff = abs(list_b[j] - list_b[j - 1])
            sum += diff
        return sum


    def get_permutation_list(self):
        """
        按照给定数组A相邻数字⼤⼩关系进⾏排列，无法看出什么关系
        :return:
        """
        permutation_list_b = []
        for i in range(self.list_len):
            pass

    def get_solution(self):
        permutation_list_b = self.get_permutation_list()
        for i in range(len(permutation_list_b)):
            sum = self.cal_max(permutation_list_b[i])
            if sum > self.max_sum:
                self.max_sum = sum
                self.max_sum_index = i

# 需求4:
# 需求描述：设计⼀个服务，任何⼈调⽤这个服务，都返回⼀个 unique id，不能重复；请尽量提⾼⽣成效率和尽量降低时间复杂度
# 1. 任何一个服务的底层都离不开网络IO模型，因此我选用异步的IO模型作为网络请求处理的核心
# 2. 返回⼀个 unique id，我选用信息摘要算法，他可以保证唯一性
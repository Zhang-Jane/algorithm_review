import random

from utils.decorator import cal_time

"""
列表分为有序区和无序区域(这俩个区域都在同一个列表进行操作)，俩个部分，最初有序的区域只要一个元素
每次从无序的区域哪一个插入到有序的区域的位置，直到最后
"""
li = [100, 2, 89, 98, 23, 76, 38, 85, 12, 9, 4]


# 时间复杂度O(n^2)
@cal_time
def insert_sort(li):
    for i in range(1, len(li)):  # 摸到的牌的下标从1开始，代表摸到牌的下标，第0个默认是最开始的有序的区域
        tmp = li[i]  # 摸到的牌的值，先存起来
        j = i - 1  # 代表的是剩下的牌的下标
        # 往后移动牌的条件：拿到的牌要比待插入的有序的区域中的值小。j>=0表示的已经到有序区域最小值，再往前走没有比较的值了
        while j >= 0 and tmp < li[j]:
            li[j + 1] = li[j]
            j -= 1
        # 在循环结束的位置，要么-1（已经到头了），要么li[j]（有序区域的值都比摸到的牌的值小，就是说你不用插入，往后插入）
        li[j + 1] = tmp

li = list(range(100))
random.shuffle(li)
# print(li)
insert_sort(li)
print(li)

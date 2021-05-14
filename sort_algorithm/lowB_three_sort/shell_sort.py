"""
[100, 2, 89, 98, 36]
100  89  46
"""
import random
from utils.decorator import cal_time


def insert_sort(li, d):
    for i in range(d, len(li)):  # 摸到的牌的下标从1开始，代表摸到牌的下标，第0个默认是最开始的有序的区域
        tmp = li[i]  # 摸到的牌的值，先存起来
        j = i - d  # 代表的是剩下的牌的下标
        # 往后移动牌的条件：拿到的牌要比待插入的有序的区域中的值小。j>=0表示的已经到有序区域最小值，再往前走没有比较的值了
        while j >= 0 and tmp < li[j]:
            li[j + d] = li[j]
            j -= d
        # 在循环结束的位置，要么-1（已经到头了），要么li[j]（有序区域的值都比摸到的牌的值小，就是说你不用插入，往后插入）
        li[j + d] = tmp

@cal_time
def shell_sort(li):
    d = len(li) // 2
    while d > 0:
        insert_sort(li, d)
        d = d // 2


li = list(range(10000))
random.shuffle(li)
# print(li)
shell_sort(li)
# print(li)

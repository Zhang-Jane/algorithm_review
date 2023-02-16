import random

from utils.decorator import cal_time
# li = [100, 89 , 98, 23, 76, 38, 85, 12, 9, 0, 4]
# li = [1 ,2 ,3, 0]
li = list(range(10000))
random.shuffle(li)
print(li)

# 时间复杂度n^2
@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break

"""
关键点在于对数列有序区的界定
在每一轮排序后，记录下来最后一次元素交换的位置，
该位置即为无序数列的边界，再往后就是有序区了。

"""
@cal_time
def bubble_sort2(li):
    # 无序数列的边界，每次比较只需要比到这里为止
    lastExchangeIndex = 0
    # 无序数列的边界，每次比较只需要比到这里为止
    sortBorder = len(li) - 1
    for i in range(len(li) - 1):
        exchange = False
        for j in range(sortBorder):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
                # 更新为最后一次交换元素的位置
                lastExchangeIndex = j
        sortBorder = lastExchangeIndex
        if not exchange:
            break


bubble_sort2(li)
print(li)

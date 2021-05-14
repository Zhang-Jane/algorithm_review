import random

from utils.decorator import cal_time
# li = [100, 89 , 98, 23, 76, 38, 85, 12, 9, 0, 4]
li = [1 ,2 ,3, 0]
# li = list(range(100))
# random.shuffle(li)
# print(li)

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


bubble_sort(li)
print(li)

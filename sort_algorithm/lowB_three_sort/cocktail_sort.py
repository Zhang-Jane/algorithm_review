"""
鸡尾酒排序的思路。
排序过程就像钟摆一样，第1轮从左到右，2轮从右到左，第3轮再从左到右…
代码外层的大循环控制着所有排序回合
大循环内包含2个小循环，第1个小循环从左向右比较并交换元素，第2个小循环从右向左比较并交换元素。
"""
import random

from utils.decorator import cal_time
# li = [100, 89 , 98, 23, 76, 38, 85, 12, 9, 0, 4]
# li = [1 ,2 ,3, 0]
li = list(range(10000))
random.shuffle(li)
print(li)


# 鸡尾酒排序，也是属于冒泡排序的一种改进方法
@cal_time
def cocktail_sort(arr):
    for i in range(len(arr) // 2):
        # 有序标记，初始为True
        flag = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = False
        if flag:
            break
        # 偶数轮开始之前，要重新标记为True
        flag = True
        # 偶数轮，从右向左比较和交换
        for k in range(len(arr) - i - 1, i, -1):
            if arr[k] < arr[k - 1]:
                arr[k], arr[k - 1] = arr[k - 1], arr[k]
                flag = False
        if flag:
            break
    return arr


cocktail_sort(li)
print(li)

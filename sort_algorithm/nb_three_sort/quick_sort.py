import random

li = [100, 2, 89, 98, 23, 76, 38, 85, 12, 9, 4]
# li = [100, 2]

# 时间复杂度O(nlogn), 最坏的n2


def quick_sort(li, left, right):
    """
    注意：快速排序是直接在原始数组里进行各种交换操作，所以当子数组被分割出来的时候，原始数组里的排列也被改变了
    :param li: 所要排序的列表
    :param left: 排序的区域的
    :param right: 排序的区域的
    :return:
    """

    if left < right and len(li) >= 2:
        mid = partition1(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


def partition(li, left, right):
    """
    1.找一个基准值（可以是固定，可以是随机的）
    2.根据这个基准值，分成俩部分，一部分比他大的放右边，比他小的放左边
    3.最后把这个基准值放回到空缺的位置，然后返回
    :param li:
    :param left:
    :param right:
    :return:
    """
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def partition1(li, left, right):
    """
     partition 函数获得基准值。

    :param li:
    :param left:
    :param right:
    :return:
    """
    p_index = random.randint(left, right)
    li[p_index], li[left] = li[left], li[p_index]
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def partition2(array, l, r):
    """
    partition函数单向扫描法
    :param array:
    :param l:
    :param r:
    :return:
    """
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


quick_sort(li, 0, len(li) - 1)
print(li)

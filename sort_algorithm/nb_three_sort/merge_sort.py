
li1 = [15, 17, 18, 20, 10, 11, 13, 14, 19]
li2 = [100, 2, 89, 98, 23, 76, 38, 85, 12, 9, 4]


def merge(li, low, mid, high):
    """
    将俩个排序好的列表，归并在一个，且排好顺序
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:  # 排好序的左边和右边比较。如果小的先放入临时的列表
            li_tmp.append(li[i])
            i += 1  # 往后移动
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    for i in range(low, high + 1):
        print(i)
        li[i] = li_tmp[i - low]


def merege_sort(li, low, high):
    """
    递归的思想解决问题，类似汉罗塔问题
    :param li: 待排序的列表
    :param low:
    :param high:
    :return:
    """
    if low < high:
        mid = (low + high) // 2
        merege_sort(li, low, mid)
        merege_sort(li, mid + 1, high)
        merge(li, low, mid, high)


# merege(li1, 0, 4, 8)
# print(li1)


merege_sort(li2, 0, len(li2) - 1)
print(li2)

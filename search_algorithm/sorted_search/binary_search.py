from utils.decorator import cal_time

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = [1, 2, 3, 3, 9, 45, 78]
"""
二分查找的中点在于low或者high中间值的范围移动，从而缩小范围。中间值的计算就是low+high的中间值，比较的结束条仔在于low和high的位置是否重合。如果重合还找不到，说明没有这个值
"""
# 时间复杂度O(logn)
# @cal_time
# def binary_search(lists, key):
#     low = 0
#     high = len(lists) - 1
#     time = 0
#     while low <= high:
#         time += 1
#         mid = int((low + high) / 2)
#         if key < lists[mid]:
#             high = mid - 1
#         elif key > lists[mid]:
#             low = mid + 1
#         else:
#             # 打印折半的次数
#             print("times: %s" % time)
#             return mid
#     print("times: %s" % time)
#     return False


# binary_search(li, 3)


def binary_search(li, target):
    if len(li) == 0:
        return -1
    left = 0  # 起始的位置，往左移最后的位置
    right = len(li) - 1  # 往右移的最后的位置
    while left <= right:
        # low + high/2 - low/2等价于（(low + high) / 2）防止了 left 和 right 太大直接相加导致溢出
        mid = int(left + (right - left) / 2)
        if li[mid] == target:
            # 往右边搜索最后要-1，往左不用
            # right = mid - 1
            left = mid + 1
        elif li[mid] > target:
            right = mid - 1
        elif li[mid] < target:
            left = mid + 1
    return left - 1


print(binary_search(li, 3))

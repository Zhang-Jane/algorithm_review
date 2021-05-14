
li = [100, 2, 89, 98, 23, 76, 38, 85, 12, 9, 4]

"""
获取最小值的位置
"""


def get_min_pos(li):
    min_pos = 0
    for i in range(1, len(li)):
        if li[i] < li[min_pos]:
            min_pos = i
    return li[min_pos]


def select_sort(li):
    for i in range(len(li) - 1):
        min_pos = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]


select_sort(li)
print(li)

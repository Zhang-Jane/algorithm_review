li = [100, 2, 89, 98, 23, 76, 38, 85, 12, 9, 4]


def quick_sort2(li):
    if len(li) < 2:
        return li
    tmp = li[0]
    left_list = [x for x in li[1:] if x < tmp]
    right_list = [x for x in li[1:] if x > tmp]

    return quick_sort2(left_list) + [tmp] + quick_sort2(right_list)


li = quick_sort2(li)
print(li)


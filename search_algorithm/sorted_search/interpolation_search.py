# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = [1, 2, 3, 7, 400000, 400001, 4000000, 40000001, 40000002, 9000000, 90000001]


def interpolation(lists, key):
    low = 0
    high = len(lists) - 1
    time = 0
    while low <= high:
        time += 1
        # 计算mid值是插值算法的核心代码
        mid = low + int((high - low) *
                        (key - lists[low]) / (lists[high] - lists[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lists[mid]:
            high = mid - 1
        elif key > lists[mid]:
            low = mid + 1
        else:
            # 打印查找的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


print(interpolation(li, 7))

from utils.decorator import cal_time
li = [2, 4, 3, 1, 6, 7, 8, 9, 0, 10]


# 时间复杂度O(n)
@cal_time
def unorder_search(lis, key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
        else:
            return False


print(unorder_search(li, 2))

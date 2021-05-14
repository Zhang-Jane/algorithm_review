li = [11,13,14,15,19,20,22,23]


def binary_search(li, key):
    low = 0
    high = len(li) - 1 # 索引从0开始
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == key: # 如果相等说明找到了这个值
            return mid
        elif key > li[mid]: # 如果所需要的值在mid的右边，则mid的下标等于low
            low = low + 1
        elif key < li[mid]:
            high = high - 1


def xx_binary_search(li, key):
    low = 0
    high = len(li) - 1 # 索引从0开始
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == key: # 如果相等说明找到了这个值
            return mid
        elif key > li[mid]: # 如果所需要的值在mid的右边，则mid的下标等于low
            low = mid
        elif key < li[mid]:
            high = mid



print(xx_binary_search(li, 22))
# print(binary_search(li, 12))
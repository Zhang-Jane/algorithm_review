"""
1. 快慢指针
2. 左右指针
"""

# head_index = 0
# left_index = 0
# right_index = 0
# fast_index = 0
# slow_index = 0



def catch_problems():
    li = [1, 2, 3, 4, 4, 6, 7, 8, 9, 10]
    for i in range(len(li) - 1):
        slow_index = i
        fast_index = i + 1
        if li[slow_index] == li[fast_index]:
            print(f"{li[slow_index]} ==> {li[fast_index]}", end=" | ")

def slide_windows():
    # li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    li = [1, 1, 3, 4, 3, 6, 0, 8, 9, -10]
    box = []
    max_val = 0
    right_index = 0
    left_index = 0
    max_len = 3
    while right_index < len(li):
        if len(box) < max_len:
            box.append(li[right_index])
        right_index += 1
        if len(box) == 3:
            max_val = max(max_val, sum(box))
            print(box)
            box.remove(min(box))
            left_index += 1
        # print(f"{li[left_index]} ==> {li[right_index]}", end=" | ")
        print(max_val)


if __name__ == '__main__':
    slide_windows()


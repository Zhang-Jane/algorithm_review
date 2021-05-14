def get_digit(num, i):
    return num // (10*i) % 10


def reverse_int(num):
    res = 0
    while num > 0:
        res = res * 10
        res += num % 10
        print(res)
        num = num // 10
    return res

print(reverse_int(1234))
def reverse_list(li):
    """
    对称交换
    1, 2, 3, 4, 5
    5, 2, 3, 4, 1
    5, 4, 3, 2, 1
    :return:
    """
    n = len(li)
    for i in range(n // 2):  # n // 2 -1（前包后不包）
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return li


def int2list(num):
    li = []
    while num > 0:
        li.append(num % 10)
        num = num // 10
    reverse_list(li)
from data_structure.Tree.build_tree import Node


def traverse_list(li: list):
    # range(结尾包含)
    # for i in range(len(li)):
    #     print(li[i])

    # len_index = len(li) - 1
    # while len_index >= 0:
    #     print(li[len_index])
    #     len_index -= 1

    len_index = len(li)
    i = 0
    while i < len_index:
        print(li[i])
        i += 1


def recurse_list(li: list, index: int):
    if index < 0:
        return -1
    # print(li[index])
    res = recurse_list(li, index - 1)
    print(res)
    print(li[index])


if __name__ == '__main__':
    li = [1, 2, 3, 6]
    recurse_list(li, len(li) - 1)

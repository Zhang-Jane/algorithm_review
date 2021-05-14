"""
二叉树的顺序存储方式（列表）
孩子找父结点(n-1)/2（这里计算机中的除以2，省略掉小数）
父节点和左孩子的关系 2n+1(n代表列表的下标索引)
父节点和右孩子的关系 2n+2(n代表列表的下标索引)
大根堆：一个完全的二叉树，满足任一节点都比其孩子节点大
小跟堆：一个完全的二叉树，满足任一节点都比其孩子节点小
升序用大根堆，降序就用小根堆
堆排序：
1.构建堆
从最最后的一个有孩子的节点构建小堆，然后依次构建。
2.堆的调整
    堆化（向下调整）、向上调整的前提都是：在二叉树中，只有一个位置不满足堆的性质，其它位置都满足堆的性质。
    向下调整 是让调整的结点与其孩子节点进行比较
    向上调整 是让调整的结点与其父亲结点进行比较
3.出数
将顶端的数与末尾的数交换，此时，末尾的数为最大值，剩余待排序数组个数为n-1
将剩余的n-1个数再构造成大根堆（堆的调整），再将顶端数与n-1位置的数交换，如此反复执行，便能得到有序数组
"""
import random
from utils.decorator import cal_time
"""
待调整的树
                    2
        9                       7
    8         5             0       1
6       4   3
[2, 9, 7, 8, 5, 0, 1, 6, 4, 3]
调整完的树
                    9
        8                       7
    6         5             0       1
2       4   3
[9, 8, 7, 6, 5, ,0, 1, 2, 4, 3]
"""


def shift_down(li, low, high):
    """
    堆的调整(大根堆)
    :param li: 树的根
    :param low: 树的根的位置
    :param high: 树的最后的一个节点的位置，表示数的范围
    :return:
    """
    tmp = li[low]  # 把根的值用临时变量先存储
    i = low  # 拿出来之后，空位的位置
    j = 2 * i + 1  # 俩个孩子的位置
    while j <= high:  # 循环退出的第二个条件：j>high，说米i是叶子节点
        if j + 1 <= high and li[j] < li[j + 1]:  # 右孩子必须存在才能j+1
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:  # 循环退出的第一个条件：j位置的值比tmp小，说明俩个孩子都比tmp小
            break
    li[i] = tmp



# li = [2, 9, 7, 8, 5, 0, 1, 6, 4, 3]
# shift_down(li, 0, len(li)-1)
# print(li)
#

def build_heap(li):
    """
    堆排序
    :return:
    """
    n = len(li)
    # 1.从最后的节点位置开始构造堆，low = (n - 1 - 1) // 2, high = n - 1
    for low in range(n // 2 - 1, -1, -1):
        shift_down(li, low, n - 1)

@cal_time
def heap_sort(li):
    n = len(li)
    build_heap(li)
    for high in range(n - 1, -1, -1):
        li[0], li[high] = li[high], li[0]
        shift_down(li, 0, high - 1)

li = list(range(10000))
random.shuffle(li)
heap_sort(li)
# print(li)

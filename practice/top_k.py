# 建立最小堆
def heap_adjust(A, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    min_index = i
    if left < size and A[left] < A[min_index]:
        min_index = left
    if right < size and A[right] < A[min_index]:
        min_index = right
    if min_index != i:
        temp = A[i]
        A[i] = A[min_index]
        A[min_index] = temp
        heap_adjust(A, min_index, size)
    return A


def build_heap(A):
    n = len(li)
    for i in range(n // 2, -1, -1):
        heap_adjust(A, i, n)
    return A


def heap_sort(li):
    n = len(li)
    build_heap(li)
    print(li)
    for high in range(n - 1, -1, -1):
        li[0], li[high] = li[high], li[0]
        heap_adjust(li, 0, high - 1)

li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
heap_sort(li)
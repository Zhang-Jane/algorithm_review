import sys
sys.setrecursionlimit(100)


# # 例子1
def func(x):
    if x > 0:
        print(x)
        m = func(x - 1) # 标记func1
        # print(f"${x}$")
        n = func(x - 1) # 标记func2
        # print(f"={x}=")
        print(m,n)
    else:
        return 0
func(3)
#
#
# # 例子2
# def func2(x):
#     print(x)
#     func2(x - 1)
# func2(10)
#
#
# # 例子3
# def func3(x):
#     if x > 0:
#         print(x)
#         func3(x - 1)
# func3(10)


# # 例子4
# def func4(x):
#     if x > 0:
#         print(x)
#         func4(x + 1)
# func4(10)

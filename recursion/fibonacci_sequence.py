from utils.decorator import cal_time
"""
f(n) = f( n - 1) + f(n - 2)  f(1)= 1  f(2)=1
1、1、2、3、5、8、13、21、34...
"""
# 时间复杂度O(2^n), 空间复杂度O(1)
def fibonacci1(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)

# 时间复杂度O(n)，空间复杂度O(n)
def fibonacci2(n):
    li = [1, 1]
    if n == 0:
        return 0
    if n <= 2:
        return li[0]
    else:
        for i in range(2, n + 1):
            print(li)
            li.append(li[-1] + li[-2])
        return li[n - 1]


# 时间复杂度O(n)，空间复杂度O(1)
def fibonacci3(n):
    a = 1
    b = 1
    c = 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c



# @cal_time
# def func():
#     result = fibonacci3(10)
#     print(result)

def func(n):
    f1 = 1
    f2 = 1
    for x in range(1, n+1):
        if x == 1:
            print(1, end=' ')
            continue
        elif x == 2:
            print(1, end=' ')
            continue
        f1, f2 = f2, f1+f2
        print(f2, end=' ')



print(fibonacci3(10))

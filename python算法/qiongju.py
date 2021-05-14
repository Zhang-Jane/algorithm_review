import itertools


def twentyfour(cards):
    """
    itertools.permutations
    返回的是列表中元素的全排列。
    高中排列组合中的那个A
    product(A, B) 和 ((x,y) for x in A for y in B)一样
    itertools.product(*iterables, repeat=1)
    iterables是可迭代对象,repeat指定iterable重复几次
    :param cards:
    :return:
    """
    '''史上最短计算24点代码'''
    for nums in itertools.permutations(cards):  # 四个数
         for ops in itertools.product('+-*/', repeat=3):  # 三个运算符（可重复！）
              # 构造三种中缀表达式 (bsd)
              bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
              bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
              bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  # a/(b-(c/d))

              for bds in [bds1, bds2, bds3]:  # 遍历
                   try:
                         if abs(eval(bds) - 24.0) < 1e-10:  # eval函数
                              return bds
                   except ZeroDivisionError:  # 零除错误！
                         continue

    return 'Not found!'


# for card in cards:
#     print(twentyfour(card))

# print(list(itertools.permutations('ABC')))
print(list(itertools.product('+-*/', repeat=3)))
nums = [1, 2, 3, 4]
ops = ('+', '+', '-')
x = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)
print(x)
"""
寻找100以内的质数
质数的特征是除了1和自身之外不能被任何数整除的正整数
任何一个整数都可以唯一表示成有限个素数的乘积
"""
"""
步骤：
范围：(2, 100]
枚举的条件：2-100，2-i-1
判断条件：x % a != 0
"""
# li = []
# for i in range(2, 1000):
#     for j in range(2, i - 1):
#         result = i % j
#         # print(f"{i} % {j} = {result}")
#         if result == 0:
#             break
#     else:
#         li.append(i)
# print(f"prime number is {li}")
# # 时间复杂度n*m

"""
孪生素数
间隔为2的素数，比如(3,5),(5,7),(71,73)
"""
"""
方案1：
枚举
方案2：
数学家的万能公式
若自然数Q与Q+2都不能被任何不大于√Q+2的素数整除，
则Q与Q+2都是素数，称为孪生素数
"""
import math
li2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
       449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
# 习惯性的从前往后数数
# for i in range(len(li2)-1):
#     if i < len(li2) - 1:
#         result2 = abs(li2[i] - li2[i+1])
#         # print(result2)
#         if result2 == 2:
#             print(f"{li2[i]} - {li2[i+1]}")

# for i in range(1, len(li2)):
#     result2 = abs(li2[i] - li2[i-1])
#     # print(result2)
#     if result2 == 2:
#         print(f"{li2[i-1]} - {li2[i]}")

"""
金蝉素数是某古寺的一块石碑上依稀刻有一些神秘的自然数。
这些数是由1，3，5，7，9 这5 个奇数字排列组成的5 位素数，且同时去掉它的最高位与最低位数字后的三位数还是素数，同时去掉它的高二位与低二位数字后的一位数还是素数。因此，人们把这些神秘的素数称为金蝉素数，喻意金蝉脱壳之后仍为美丽的金蝉
"""


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num - 1):
        result = num % i
        if result == 0:
            return False
    else:
        return True


def is_prime2(num):
    """
    如果 m 不能被 2 ~ √m间任一整数整除，m 必定是素数
    因为任何一个数都能被分解，约数是成对出现的。这对约数必须一个在根号n之前，一个在根号n之后，不然俩个约数会大于这个数
    16 能被 2、4、8 整除，16=2*8，2 小于 4，8 大于 4，16=4*4
    只需判定在 2~4 之间有无因子即可。
    """
    if num <= 1:
        return False
    k = int(math.sqrt(num) + 1)
    for i in range(2, k):
        result = num % i
        if result == 0:
            return False
    if i >= k:
        return True


x = []


def reverse_num(num):
    if num <= 0:
        return x
    last_bit = num % 10
    x.append(last_bit)
    return reverse_num(num // 10)


new_num = 0


def reverse_num(num):
    global new_num
    if num <= 0:
        return new_num
    last_bit = num % 10
    new_num *= 10
    new_num += last_bit
    return reverse_num(num // 10)


print(reverse_num(124))

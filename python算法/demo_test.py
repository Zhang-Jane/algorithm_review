import heapq
from collections import Counter
import inspect

# source = inspect.getsource(Counter)
# print(source)

# seq = ('Google', 'Runoob', 'Taobao', 'Taobao', 'Taobao', 'Google')

# c = Counter(seq)
# print(c.most_common(2))
# x = zip([1, 2, 3], [4, 5, 6])
# x = [1, 2, 3]
# def a(args):
#     print(*args)
# a(x)
a_dic = {'a':1, 'b':4, 'A':6}
# b_dict = sorted(zip(a_dic.keys(), a_dic.values()), reverse = True)
# print(b_dict)
from operator import itemgetter

b_dict = sorted(a_dic.items(), key=itemgetter(1), reverse=True)
print(b_dict)
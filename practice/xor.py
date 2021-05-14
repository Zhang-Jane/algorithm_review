"""
异或逻辑运算的规律:
0⊕0=0,0⊕1=1
1⊕0=1,1⊕1=0
相同取0，相异取1
0和任何数疑惑都是它本身
"""
# 异或运算及其应用-查找奇数个数的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""
1. a ^ b = b ^ a
2. a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c
3. d = a ^ b ^ c 可以推出 a = d ^ b ^ c
4. a ^ b ^ a = b
"""
li = [2, 2, 3, 3, 8]
a = 0
for i in li:
    a = a ^ i
print(a)
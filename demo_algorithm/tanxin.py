def main():
    d = [0.01,0.02,0.05,0.1,0.2,0.5,1.0] # 存储每种硬币的面值
    print(d)
    d_num = [] # 存储每种硬币的数量
    s = 0
    # 拥有的零钱总和
    # temp = input('请输入每种零钱的数量：')
    d_num0 = [12, 11, 11, 11, 11, 11, 11]

    for i in range(0, len(d_num0)):
          d_num.append(int(d_num0[i]))
          s += d[i] * d_num[i] # 计算出收银员有多少钱
    print(s)
    sum = float(input("请输入需要找的零钱："))

    if sum > s:
         # 当输入的总金额比收银员的总金额多时，无法找零
         print("数据有错")

         return 0

    s = s - sum
    # 要想用的硬币数量最少，需要利用所有大面值的硬币，因此从数组的大面值的元素开始遍历
    i = 6
    while i >= 0:
         if sum >= d[i]:
              n = int(sum / d[i])
              if n >= d_num[i]:
                   n = d_num[i]  # 更新n
              sum -= n * d[i] # 贪心算法的关键步骤，令sum动态改变
              print("用了%d个%f枚硬币"%(n, d[i]))
         i -= 1

if __name__ == "__main__":
     main()
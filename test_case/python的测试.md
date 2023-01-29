## 调试和测试
1. print输出，简单粗暴
2. 断言assert，Python内置了一个assert关键字，表示断言。用来判断表达式，如果表达式为True，那就什么都不做，程序接着往下走；如果False，那么就会弹出异常Traceback
3. 日志logging，logging是Python内置的一个日志模块
4. unittest，pytest

pytest 测试框架和 when-changed 文件变动监控工具(方便我们修改完代码保存后自动执行测试)或者pip install watchdog
pip install https://github.com/joh/when-changed/archive/master.zip
-r 递归监听
-v 详细的输出。多个-v选项增加了冗长。最大值是3:-vvv。
-1 如果在运行命令时文件发生了更改，请不要重新运行命令
-s 在启动时立即运行命令
-q 安静地运行命令
```python
import os
#调用Linux的开门狗，实时监测，在改变代码时save以后，重新运行，配合pytest使用
os.system("when-changed -v -r -1 -s . pytest singlelink.py")
```
## 防止栈溢出
递归暴栈(栈溢出)
```python
import sys
print(sys.getrecursionlimit()) # 我的 mac 机器上输出 1000
sys.setrecursionlimit(100000) # 设置函数栈深度足够大，避免栈溢出错误
```
"""
进程和线程都会面临着内核态和用户态的切换问题耗费切换时间
协程就是用户自己控制切换时机，比如在执行函数A时，随时中断，去执行函数B，然后继续从A函数中断的地方执行
"""
from inspect import getgeneratorstate


def simple_coroutine():
	print('启动协程')
	y = 10
	x = yield y
	print('-> 协程接收到了x的值:', x)


coroutine = simple_coroutine()
print(getgeneratorstate(coroutine))  # GEN_CREATED
res = next(coroutine)
print(getgeneratorstate(coroutine))  # GEN_SUSPENDED
print(res) # 10
coroutine.send(100)  # -> 协程接收到了x的值: 100
print(getgeneratorstate(coroutine))  # GEN_CLOSED 
"""
协程有四种状态
GEN_CREATED 等待开始执行
GEN_RUNNING 协程正在执行
GEN_SUSPENDED yield处暂停
GEN_CLOSED 协程结束
"""
"""
内嵌函数引用了外部函数的变量，就会形成一个闭包
形成闭包函数的三个条件
1.必须有个内嵌函数
2.内嵌函数引用外部变量
3.外部函数返回内嵌函数
作用 保持当前运行环境
"""

def out():
	x = 5
	def inner():
		nonlocal x
		x *= x
		return x
	return inner

a = out()
print(a())

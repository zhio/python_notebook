"""
hasattr:
判断一个对象是否有某个属性或者某个方法，返回bool值
"""


class A:
	name = '小明'
	def __init__(self):
		age = 18

	def run(self):
		pass

print(hasattr(A, 'name'))  # True
print(hasattr(A, 'run'))   # True
print(hasattr(A, 'age'))   # False


"""
getattr:
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号
"""


class B:
	name = '小明'

	def run(self):
		print(self.name, 'run run run')


print(getattr(B, 'name'))  # 小明
print(getattr(B, 'run'))  # <function B.run at 0x000002CBB20E1488>
print(getattr(B, 'age', 18))  # 18


"""
setattr:
给对象的属性赋值，若属性不存在，先创建再赋值。
"""


class C:
	name = '小明'

	def run(self):
		print(self.name, 'run run run')


setattr(C, 'age', 20)
print(getattr(C, 'age'))  # 20
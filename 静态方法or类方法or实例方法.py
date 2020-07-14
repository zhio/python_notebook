def foo(x):
	print('普通的函数{}'.format(x))


class A:
	def foo(self, x):
		print('实例方法{}'.format(x))

	@classmethod
	def cls_foo(cls, x):
		print('类方法{}'.format(x))

	@staticmethod
	def static_foo(x):
		print('静态方法{}'.format(x))

a = A()
a.foo(1)
a.cls_foo(1)
a.static_foo(1)
# A.foo(1) 实例方法类不可直接调用
A.cls_foo(1)
A.static_foo(1)

"""
总结：
类方法 第一个参数为cls 静态方法不需要 实例方法为self
类不可以直接调用实例方法
静态方法和普通函数一样，只不过是放在了类中
"""
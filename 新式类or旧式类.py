# 新式类
class A(object):
	pass

# 旧式类
class B:
	pass


"""
新式类继承自object,python3中全是新式类 可以省略object
多继承mro顺序不一样 新式类采用广度遍历 旧式类采用深度遍历
新式类用super关键字继承构造方法，经典类用 父类.init（self）来继承
"""
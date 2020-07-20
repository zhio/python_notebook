"""
运行时获取对像的类型
"""
a = [1]	
print(type(a))  # <class 'list'>
print(isinstance(a, list))  # True
print(dir(a))  # 获取a拥有的方法
print(hasattr(list, '1'))  # False
print(getattr(list, 'pop')) # <method 'pop' of 'list' objects>

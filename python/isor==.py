"""
is 是判断内存地址是否一样
== 是判断值是否一样
"""
a = [1, 2, 3]
b = a[::]
print(a is b)  # False
print(a == b)  # True
print(id(a))  # 2986891305608
print(id(b))  # 2986891305672
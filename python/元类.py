"""
python一切皆对象，类也是对象。创建类的类就是元类，元类是创建类的工厂。
python中大多数内置的类的元类都是type
type和object关系：type是object的子类，而object又是type的实例
"""

print(str.__class__)
print(object.__class__)
print(type.__class__)
print(type.__mro__)
"""
1.用法不同
__new__用来创建类的实例，在实例创建之前调用，是类级别的方法，是个静态方法
__init__用来初始化实例，该方法是在实例对象创建后被调用，它是实例级别的方法，用于设置对象属性的一些初始值
2.参数不一样
__new__至少有一个cls参数，代表当前类
__init__至少有一个参数self，代表当前实例，是new返回的实例
3.返回值不同
__new__必须有返回值，返回实例对象
__init__不需要有返回值


__new__和__init__的区别，说法正确的是？ （ABCD）

A. __new__是一个静态方法，而__init__是一个实例方法
B. __new__方法会返回一个创建的实例，而__init__什么都不返回
C. 只有在__new__返回一个cls的实例时，后面的__init__才能被调用
D. 当创建一个新实例时调用__new__，初始化一个实例时用__init__


【__new__的作用】

依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。
首先我们来看一下第一个功能，具体我们可以用int来作为一个例子：
假如我们需要一个永远都是正数的整数类型，通过集成 int，我们可能会写出这样的代码。

"""

class Person(object):
    def __init__(self,name,age) -> None:
        print("in __init__")
        self.name = name
        self._age = age

p = Person("Gao",99)

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass

class Apple(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("apple is in red")

class Orange(Fruit):
    def __init__(self):
        pass

    def print_color(self):
        print("orange is in orange")

class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()

fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
fruit1.print_color()    
fruit2.print_color()   
# Python中的下划线

Python中有五种下划线，每种意义不一样。

## 单下划线( _ )

单下划线表示变量不需要，忽略特定的值，这只是一种约定，并不是真正的抛弃了。

示例

```python
for _ in range(2):
    print("hello")

"""
hello
hello
"""
```

注意，_并没有抛弃值

```python
for _ in range(2):
    print("hello")
    print(_)

"""
hello
0
hello
1
"""
```

## 单前导下划线（_var)

单前导下划线也是一种约定，告诉程序员以单下划线开头的变量或者方法，只可以在内部使用，表示私有的，对程序没有影响。

示例

```python
class Test:
    def __init__(self):
        self.name = "xiaoming"
        self._age = 18


if __name__ == '__main__':
    t = Test()
    print(t.name)  # xiaoming
    print(t._age)  # 18
```

可以看到`_age`在外部也是可以访问到的，仅起到约定作用，表示私有的，对程序没有影响。

## 双前导下划线(\_\_var)

对于双前导下划线开头的变量和方法， Python解释器会重写属性名称，避免与子类中的命名冲突。

示例:

```python
class Test:
    def __init__(self):
        self.name = "xiaoming"
        self.__age = 18


if __name__ == '__main__':
    t = Test()
    print(t.name)
    print(t.__dict__)
    # print(t.__age)  # 会报错

"""
xiaoming
{'name': 'xiaoming', '_Test__age': 18}
"""
```

可以看到`__age`被重写成`_Test__age`这样做的目的就是防止与子类定义的名称冲突

## 双前导和双末尾下划线（\_\_var\_\_）

双前导和双末尾定义的变量，是Python中内置的魔法方法，有特殊的作用。如\_\_new\_\_方法用来创建类。

## 单末尾下划线(var_)

有时候，一个变量的最合适的名称已经被一个关键字所占用,这种情况下可以加一个下划线来解决命名冲突。

示例：

```Python
def func(name, class_):
    pass
```

## 总结

| 下划线                              | 作用                                   |
| ----------------------------------- | -------------------------------------- |
| 单下划线( _ )                       | 用作无用的变量占位                     |
| 单前导下划线（_var)                 | 约定的私有属性或方法                   |
| 双前导下划线(\_\_var)               | 会被Python解释器重新命名，触发名称修饰 |
| 双前导和双末尾下划线（\_\_var\_\_） | 魔法方法                               |
| 单末尾下划线(var_)                  | 约定避免与关键字冲突                   |



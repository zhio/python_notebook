# Python中的函数重载

首先要明确函数重载要解决的问题

	- 参数类型不同
	- 参数个数不同

对于参数类型不同这种情况，Python中可以接收任意类型的参数，也就无法根据参数类型来支持重载

对于参数个数不同这种情况，Python中有缺省参数(参数名=默认值)处理。

基于这些，Python无需函数重载，都可以在函数内部进行判断处理，但是有些时候在函数内部处理不够pythonic，在Python3.4中提供了转发机制来实现重载。

示例

```python
from functools import singledispatch


@singledispatch
def func(obj):
    print("%r" % obj)


@func.register(int)
def _(obj):
    print("int :%d" % obj)


@func.register(str)
def _(obj):
    print("string :%s" % obj)


@func.register(list)
def _(obj):
    print("list :%r" % obj)


if __name__ == '__main__':
    func("hello")
    func(1)
    func([1,3,4])
    func(object)
    
    
"""
string :hello
int :1
list :[1, 3, 4]
<class 'object'>
"""
```

对比一下不使用函数重载

```python
def func(obj):
    if isinstance(obj, int):
        print("int :%d" % obj)
    elif isinstance(obj, str):
        print("string :%s" % obj)
    elif isinstance(obj, list):
        print("list :%r" % obj)
    else:
        print("%r" % obj)


if __name__ == '__main__':
    func("hello")
    func(1)
    func([1,3,4])
    func(object)

    
"""
string :hello
int :1
list :[1, 3, 4]
<class 'object'>
"""
```

可以看出当类型很多的时候，写法不够Pythonic，有时候函数重载机制还是很有必要的
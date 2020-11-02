# *args和**kwargs

`*args`和`**kwargs`主要用于函数定义，当不确定参数的个数时候，可以使用。

## args

args实质是将函数传入的参数存储在args这个元组类型的变量上。

示例:

```python
def func(a, b, *args):
    print("a={},b={},args={}, args的类型:{}".format(a, b, args, type(args)))


func(1, 2, 3, 4, 5, 6)
# 结果
"""
a=1,b=2,args=(3, 4, 5, 6), args的类型:<class 'tuple'>
"""
```

可以看到传递6个参数，前两个被a,b接收，剩下的参数已元组的形式被args接收。

args另一个作用就是可以序列解包，准确来说是`*`运算符有这个作用。

示例：

```python
def func2(a, b, c):
	print("a={},b={},c={}".format(a, b, c))


li = [1, 3, 2]
func2(*li)  # a=1,b=3,c=2
```

## kwargs

args实质是将函数传入的参数以key-value形式存储在kwagrs变量上，本质是dict。

示例:

```python
def func1(a, b, **kwargs):
    print("a={},b={},kwargs={}, kwargs的类型:{}".format(a, b, kwargs, type(kwargs)))


func1(1, 2, aa=1, bb=2, cc=3)
# 结果
"""
a=1,b=2,kwargs={'aa': 1, 'bb': 2, 'cc': 3}, kwargs的类型:<class 'dict'>
"""
```

可以看到传递5个参数，前两个被a,b接收，剩下的参数已dict的形式被kwargs接收。

`**`也可以用来给dict类型进行解包。

示例:

```python
def func3(a, b, c):
	print("a={},b={},c={}".format(a, b, c))


li = {'a': 1, 'b': 2, 'c': 3}
func3(**li)  # a=1,b=3,c=2
```

## 组合使用

\*\*args 和 \*\*kwargs 是不定长参数收集机制,也就是说如果形参中指定了这两个,在调用函数的时候可以任意地向里面丢入无限多实参.这里面有一个规则就是`*args`一定要在`**kwargs`的前面

示例：

```python
def func1(a, b, *args, **kwargs):
    print("a={},b={},args={}, kwargs:{}".format(a, b, args, kwargs))


func1(1, 2, 3, 4, aa=1, bb=2, cc=3)

"""
a=1,b=2,args=(3, 4), kwargs:{'aa': 1, 'bb': 2, 'cc': 3}
"""
```

## 总结

- args是使用元组形式接收不定长参数，kwargs使用dict形式接收不定长参数
- 组合使用时，args一定要在kwarg前面
# Python2和3的区别

## print

在Python2中，print是表达式

```python
print "hello"
```

在Python3中，print是函数

```python
print("hello")
```

## 编码方式

在Python2中，默认使用ASCII编码

在Python3中，默认使用的是Unicode编码

## 除法运算

在Python2中除法运算，只保留整数，向下取整

```python
8 / 3 # 2
```

在Python中除法运算，保留小数

```python
8 / 3 # 2.666
```

## 异常捕获

在python2中，异常语法

```python
except Exception,e
```

在Python3中，异常语法

```python
except Exception  as e
```

## range

在Python2中xrange返回一个生成器对象，range返回list集合

```python
>>>xrange(1,5)
xrange(1, 5)

>>>list(xrange(1,5))
[1, 2, 3, 4]
```

在Python3中取消了xrange，只有range，返回生成器对象

```python
>>> range(10)
range(0, 10)
```

## input

在Python2中raw_input把所有的输入当做字符串对待，input只能接受数字的输入

在Python3中只有input，可以接受字符串和数字，返回字符串

## 新式类

在Python2中使用的是经典类，只有显示继承object才是新式类

在Python3中使用的只有新式类

## nonlocal

在Python2中，无法实现嵌套函数中的变量声明为非局部变量

在Python3中，增加了nonlocal关键字，可以把嵌套函数的变量提升

```python
def func():
    c = 1
    def foo():
        nonlocal c
        c = 10
    foo()
    print(c)
func()  # 10
```


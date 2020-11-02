# lambda表达式

## 匿名函数

匿名函数，通俗的说就是没有名字的函数，功能比较简单。Python中使用lambda表达式来创建匿名函数。

lambda表达式有以下特点：

- 可以接受任意多个参数并且返回单个表达式的值
- 只允许包含一个表达式，不能包含复杂语句
- 表达式的结果就是函数的返回值
- lambda实际上生成的是函数对象，而def定义的普通函数是把生成的函数对象赋值给变量了（这个变量就是函数名）

示例：

```python
f = lambda x: x * 2
print(f(2))  # 4
```

## 使用场景

- 把lambda表达式赋值给变量，通过变量间接调用

  例如，执行语句add=lambda x, y: x+y，定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1,2)，输出为3。

- 将lambda表达式赋值给其他函数，从而使其他函数用lambda替换

  例如，为了把标准库time中的函数sleep的功能屏蔽(Mock)，我们可以在程序初始化时调用：time.sleep=lambda x:None。这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做。

- 把lambda表达式作为参数传递给其他函数

  比如内置的filter、sorted、map、reduce函数
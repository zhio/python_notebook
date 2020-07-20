"""
不定长参数
当有多余参数时 args会已元组形式接受 kwargs相当于dict
*args和**kwargs可以同时在函数的定义中,但是*args必须在**kwargs前面.
还可以用来序列解包
"""


def func(a, b, *args):
	print("a={},b={},args={}".format(a, b, args))


func(1, 2, 3, 4, 5, 6)  # a=1,b=2,args=(3, 4, 5, 6)


def func1(a, b, **kwargs):
	print("a={},b={},kwargs={}".format(a, b, kwargs))


func1(1, 2, aa=1, bb=2, cc=3)  # a=1,b=2,kwargs={'aa': 1, 'bb': 2, 'cc': 3}


def func2(a, b, c):
	print("a={},b={},c={}".format(a, b, c))


li = [1, 3, 2]
func2(*li)  # a=1,b=3,c=2


def func3(a, b, c):
	print("a={},b={},c={}".format(a, b, c))


li = {'a': 1, 'b': 2, 'c': 3}
func3(**li)  # a=1,b=3,c=2
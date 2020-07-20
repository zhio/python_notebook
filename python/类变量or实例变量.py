class Test:
	num = 0
	def __init__(self, name):
		self.name = name
		self.num  += 1


print(Test.num)  # 0
t1 = Test('小明')
print(t1.name, t1.num)  # 小明 1
print(Test.num)  # 0
t2 = Test('小李')
print(t2.name, t2.num) # 小李 1
print(Test.num)  # 0


class Person:
	name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa


class Per:
	name = []


p1 = Per()
p2 = Per()
p1.name.append(1)
print(p1.name)  # [1]
print(p2.name)  # [1]


"""
类变量是所有的实例共享的变量
实例变量是每个实例独有的变量
"""

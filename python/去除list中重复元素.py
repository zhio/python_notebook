"""
去除list中的重复元素
"""

# 第一种 内置set
l = [1, 1, 4, 3, 1, 4]
print(list(set(l)))
print(sorted(set(l), key=l.index))

# 第二种 循环，使用临时列表
temp = []
for i in l:
	if i not in temp:
		temp.append(i)
print(temp)

# 第三种使用dict
d = {}
d = d.fromkeys(l)
print(list(d.keys()))
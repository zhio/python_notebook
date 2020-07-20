# 列表推导式
lis = [i for i in range(10)]
print(lis)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 字典推导式
d = {"A":"1","B":"2"}
dic = {v: k for k, v in d.items()}
print(dic)  # {'1': 'A', '2': 'B'}
# 生成器推导式
gen = (i for i in range(10))
print(gen)  # <generator object <genexpr> at 0x00000244CFCD4048>
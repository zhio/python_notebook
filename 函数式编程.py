# filter 过滤器

print(list(filter(lambda x : x % 2 == 0, [i for i in range(10)]))) # [0, 2, 4, 6, 8]

# map 对每一项执行函数

print(list(map(lambda x : x * 2, [i for i in range(10)]))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# reduce函数是对一个序列的每个项迭代调用函数
from functools import reduce

print(reduce(lambda x, y: x + y, [i for i in range(10)]))  # 45

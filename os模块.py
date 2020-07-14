import os


# ---------------系统操作-------------

# 获取操作系统信息 windows系统nt linux posix
print(os.name)  # nt
# 读取环境变量
print(os.getenv('PATH'))
# 获取当前路径
print(os.getcwd())

# ---------------文件目录操作-------------

# 列出指定目录下所有的目录和文件
print(os.listdir('D:\\'))  # ['python', '1.py']

# 创建目录
# print(os.mkdir('D:\\yes'))

# 删除一个空目录
# print(os.rmdir('D:\\yes'))

# 递归创建目录
# print(os.makedirs('D:\\yes\\no'))

# 递归删除空目录
# print(os.removedirs('D:\\yes\\no'))

# 切换目录
# print(os.chdir('D:\\'))

# 重命名文件
# print(os.rename('D:\\yes', 'D:\\no'))


# ---------------path模块-------------

# 判断文件路径是否存在
print(os.path.exists('D:\\yes'))

# 判断是否为文件
print(os.path.isfile('D:\\yes'))

# 判断是否为目录
print(os.path.isdir('D:\\yes'))

# 返回文件名
print(os.path.basename('D:\\yes'))

# 返回文件路径
print(os.path.dirname('D:\\yes'))

# 返回文件大小
print(os.path.getsize('D:\\yes'))

# 获取绝对路径
print(os.path.abspath('D:\\yes'))

# 拼接文件名或者路径
print(os.path.join('D:\\yes', 'yas'))
"""
cookie存放在客户端，session存放在服务器
cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗，考虑到安全应当使用session。
session存在服务器上，访问增多，对性能有影响
单个cookie保存不能超过4k

"""
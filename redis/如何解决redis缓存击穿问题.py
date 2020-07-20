"""
缓存击穿主要是热点key失效，大量请求打到后端
解决：
设置热点key用不过期
加互斥锁，缓存中没有热点key对应的数据时，等待100ms，由获得锁的线程去读取数据库然后设置缓存。
"""
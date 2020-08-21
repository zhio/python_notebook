#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 * @Author: chenjb
 * @Date: 2020/6/24 11:18
 * @Last Modified by:   chenjb
 * @Last Modified time: 2020/6/24 11:18
 * @Desc:
"""
import threading
"""
单例模式：保证创建的类只有一个实例
适用场景：线程池、连接池，资源共享 日志文件，应用配置
         要频繁实例化然后销毁的对象
优缺点： 在内存里只有一实例，减少了内存开销。一个对象需要频繁创建和销毁，无法优化
        可以避免对资源的多重占用。对同一个文件的写操作

        没有接口，不能扩展

"""


# 装饰器实现


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class Foo:
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True


# 使用基类 New 是真正创建实例对象的方法，所以重写基类的new 方法，以此保证创建对象的时候只生成一个实例


class Singleton:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True


# 元类，元类是用于创建类对象的类，类对象创建实例对象时一定要调用call方法，因此在调用call时候保证始终只创建一个实例即可，type是python的元类


class Singleton1(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton1):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True
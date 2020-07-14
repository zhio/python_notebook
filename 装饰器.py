"""
装饰器的作用就是为已经存在的对象添加额外的功能。                                                                                                                                                                                                                                                                                                                                                                                                                                                            
"""

import time


def log_time(func):
	def _log(*args, **kwargs):
		beg = time.time()
		res = func(*args, **kwargs)
		print('use time:{}'.format(time.time() - beg))
		return res
	return _log


@log_time
def func():
	time.sleep(2)


func()


class LogTime(object):
	
	def __call__(slef, func):
		def _log(*args, **kwargs):
			beg = time.time()
			res = func(*args, **kwargs)
			print('use time:{}'.format(time.time() - beg))
			return res
		return _log

@LogTime()
def func1():
	time.sleep(3)


func1()
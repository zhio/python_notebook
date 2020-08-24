"""
线程同步:
	多线程间共享全局变量，多个线程对该变量执行不同的操作时，该变量最终的结果可能是不确定
"""

"""
方式一：
	加锁 Lock和Rlock
"""
import threading
import time


# class MyThread(threading.Thread):
# 	def __init__(self):
# 		threading.Thread.__init__(self)

# 	def run(self):
# 		global x
# 		# 获取锁
# 		lock.acquire()
# 		for i in range(3):
# 			x += i
# 		time.sleep(2)
# 		print(x)
# 		# 释放锁
# 		lock.release()


# # 创建锁
# lock = threading.RLock()

# t1 = []
# for _ in range(10):
# 	t = MyThread()
# 	t1.append(t)
# x = 0
# for i in t1:
# 	i.start()

"""
方式二：
	condition对象 使用Condition对象可以在某些事件触发后才处理数据，可以用于不同线程之间的通信或通知
方法	描述
acquire()	获取底层锁。此方法等待底层锁被解锁，将其设置为locked并返回True。
notify(n=1)	在此条件下最多唤醒n个等待的任务(默认为1)。如果没有任务在等待，则该方法是no-op。必须在调用此方法之前获取锁，并在调用后不久释放锁。如果使用未锁定的锁调用，则会引发RuntimeError错误。
locked()	如果获得了底层锁，则返回True。
notify_all()	唤醒所有在此条件下等待的任务。此方法的作用类似于notify()，但会唤醒所有等待的任务。必须在调用此方法之前获取锁，并在调用后不久释放锁。如果使用未锁定的锁调用，则会引发RuntimeError错误。
release()	释放底层锁。当在未锁定的锁上调用时，将引发RuntimeError。
wait()	等待通知。如果调用此方法时调用任务没有获得锁，则会引发RuntimeError。这个方法释放底层锁，然后阻塞它，直到它被notify()或notify_all()调用唤醒。一旦被唤醒，条件将重新获得锁，该方法将返回True。
wait_for(predicate)	等待predicate变为true。predicate必须是可调用的，其结果将被解释为布尔值。最后一个值是返回值。
"""

# import threading


# class Producer(threading.Thread):
# 	"""生产者类"""

# 	def __init__(self, thread_name):
# 		threading.Thread.__init__(self, name=thread_name)

# 	def run(self):
# 		global x
# 		# 获取锁
# 		condition.acquire()
# 		if x == 20:
# 			# 等待通知
# 			condition.wait()
# 		else:
# 			print("\nProducer: ", end=' ')

# 		for i in range(20):
# 			print(x, end=' ')
# 			x += 1
# 		print(x)
# 		condition.notify()
# 		condition.release()


# class Consumer(threading.Thread):
# 	"""消费者类"""
# 	def __init__(self, thread_name):
# 		threading.Thread.__init__(self, name=thread_name)

# 	def run(self):
# 		global x
# 		# 获取锁
# 		condition.acquire()
# 		if x == 0:
# 			# 等待通知
# 			condition.wait()
# 		else:
# 			print("\nConsumer: ", end=' ')

# 		for i in range(20):
# 			print(x, end=' ')
# 			x += 1
# 		print(x)
# 		condition.notify()
# 		condition.release()

		

# # 创建condition对象
# condition = threading.Condition()
# x = 0
# p = Producer('Producer')
# c = Consumer('Consumer')
# p.start()
# c.start()
# p.join()
# c.join()
# print('After Producer and Consumer all done:', x)

"""
方式三：
	queue
"""
# import queue
# import threading


# def worker():
# 	while True:
# 		item = q.get()
# 		if item is None:
# 			break
# 		print(item)
# 		q.task_done()

# q = queue.Queue()
# threads = []
# for i in range(3):
# 	t = threading.Thread(target=worker)
# 	t.start()
# 	threads.append(t)


# for item in range(10):
# 	q.put(item)

# q.join()

# for i in range(3):
# 	q.put(None)

# for t in threads:
# 	t.join()


"""
方式四：
	event对象 个线程设置Event对象，另一个线程等待Event对象。

"""
import threading


class Mythread(threading.Thread):

	def __init__(self, thread_name):
		threading.Thread.__init__(self, name=thread_name)

	def run(self):
		global my_event
		if my_event.isSet():
			my_event.clear()
			my_event.wait()
			print(self.getName())
		else:
			print(self.getName())
			my_event.set()


my_event = threading.Event()
my_event.set()

t1 = []
for i in range(10):
	t = Mythread(str(i))
	t1.append(t)

for i in t1:
	i.start()
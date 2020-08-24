"""
线程执行方式：
	1、setDaemon = Fasle 非守护进程，主线程结束，就会退出，子线程继续执行，直到自己任务执行完毕
"""
# import threading
# import time


# def thread():
# 	time.sleep(2)
# 	print("子线程执行完毕")


# def main():
# 	t = threading.Thread(target=thread)
# 	t.start()
# 	print('主线程结束')


# if __name__ == '__main__':
# 	main()
	# 主线程结束
    # 子线程执行完毕


"""
	2、setDaemon = True,守护进程 主线程一旦执行结束，则全部子线程被强制终止
"""
# import threading
# import time


# def thread():
# 	time.sleep(2)
# 	print("子线程执行完毕")


# def main():
# 	t = threading.Thread(target=thread)
# 	# 设置子线程为守护进程
# 	t.setDaemon(True) 
# 	t.start()
# 	print('主线程结束')


# if __name__ == '__main__':
# 	main()
# 	# 主线程结束


"""
	3、join 主线程任务结束以后，进入堵塞状态，一直等待所有的子线程结束以后，主线程再终止。
"""
import threading
import time


def thread():
	time.sleep(2)
	print("子线程执行完毕")


def main():
	t = threading.Thread(target=thread)
	# # 设置子线程为守护进程
	t.setDaemon(True) 
	t.start()
	# 主线程阻塞1s,然后主线程结束，子线程继续执行
	# 如果不设置timeout就等子线程结束主线程再结束
	# 如果设置了setDaemon=True和timeout=1主线程等待1s后会强制杀死子线程，然后主线程结束
	t.join(timeout=1)
	print('主线程结束')


if __name__ == '__main__':
	main()
	# 主线程结束
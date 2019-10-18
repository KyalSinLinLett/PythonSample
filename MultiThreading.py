# import _thread
# import time

# def print_time(thread_name, delay):
# 	count = 0
# 	while count < 5:
# 		time.sleep(delay)
# 		count += 1
# 		print("%s : %s" % (thread_name, time.ctime(time.time())))

# try:
# 	_thread.start_new_thread(print_time, ("Thread-1", 2, ))
# 	_thread.start_new_thread(print_time, ("Thread-2", 4, ))
# except:
# 	print("Error: unable to start new thread")

# while 1:
# 	pass

# import threading
# import time

# exitFlag = 0

# class myThread(threading.Thread):
# 	def __init__(self, threadID, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter

# 	def run(self):
# 		print("Starting " + self.name)
# 		print_time(self.name, self.counter, 5)
# 		print("Exiting " + self.name)

# def print_time(thread_name, delay, counter):
# 	while counter:
# 		if exitFlag:
# 			thread_name.exit()
# 		time.sleep(delay)
# 		print("%s : %s" % (thread_name, time.ctime(time.time())))
# 		counter -= 1

# thread1 = myThread(1, "Thread1", 1)
# thread2 = myThread(2, "Thread2", 2)

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Exiting main thread")

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
	print('Sleeping {} second(s)...'.format(seconds))
	time.sleep(seconds)
	return 'done sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = []

for _ in range(10):
	t = threading.Thread(target=do_something, args=[1.5])
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
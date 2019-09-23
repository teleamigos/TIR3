import time
from threading import Thread

def f():
    print("------")
    u=1+2**2000
    print(u)
    l=u/3
    print('------',l)

thread1=Thread(target=f)
start=time.time()
thread1.start()
print("running")
print("next")
thread1.join()

'''
含有参数的进程函数示列
'''

from multiprocessing import Process
from time import sleep

#含有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")


# #创建进程   位置传参 args=(,)
# p = Process(target=worker,args=(2,"LC"))

#关键字传参 kwargs={}
p = Process(target=worker,kwargs={"name":"LC","sec":2})

p.start()
p.join()
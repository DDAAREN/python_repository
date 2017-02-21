#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import threading, time

def doWaiting():
    print 'start waiting3S:\t'+time.strftime('%H:%M:%S')+"\n"
    time.sleep(3)
    print 'stop waiting3S:\t\t'+time.strftime('%H:%M:%S')+'\n'

def doWaiting1():
    print 'start waiting8S:\t'+time.strftime('%H:%M:%S')+"\n"
    time.sleep(8)
    print 'stop waiting8S:\t\t'+time.strftime('%H:%M:%S')+'\n'

tsk = []

thread1 = threading.Thread(target= doWaiting)
thread1.start()
tsk.append(thread1)
thread2 = threading.Thread(target= doWaiting1)
thread2.start()
tsk.append(thread2)

for tt in tsk:
    print 'start join %s:\t'%tt.name + time.strftime('%H:%M:%S') + '\n'
    tt.join(3)
    print tt.name +' '+ ('True' if tt.isAlive() else 'False')
    print 'end join %s:\t'%tt.name + time.strftime('%H:%M:%S') + '\n'
    print '======='

print "master end!\t\t"+ time.strftime('%H:%M:%S')

# ===

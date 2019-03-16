import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: "+ name + " started\n")
    tLock.acquire()
    print(name + " has acquired the lock\n")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time()))+ "\n")
        repeat-=1
    print(name + " is releasing the lock\n")
    tLock.release()
    print("Timer: "+name+" Completed\n")

def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 3))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 3))
    t1.start()
    t2.start()

    print("Main completed\n")

if __name__ == '__main__':
    Main()


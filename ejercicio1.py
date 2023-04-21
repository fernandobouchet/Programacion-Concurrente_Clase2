import threading
import time

def funcion():
    i=0
    while i<5:
        i =i+1
        print(i)
        time.sleep(2)

thread_1 = threading.Thread(target=funcion)
thread_2 = threading.Thread(target=funcion)

thread_1.start()
thread_2.start()


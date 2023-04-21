import threading
import time

def funcion():
    print("hola el hilo "+threading.currentThread().name)
    time.sleep(4)
thread_1 = threading.Thread(target=funcion)
thread_2 = threading.Thread(target=funcion)

thread_1.start()
thread_2.start()

print("hay en ejecucion "+str(threading.activeCount())+" hilos")
print("Los hilos son")
print(threading.enumerate())

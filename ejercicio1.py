import threading
import time

def algunHilo():
    print("\nHilo actual: {}".format(threading.current_thread()))
    print("\nHilo principal: {}".format(threading.main_thread()))


hilo_1 = threading.Thread(target=algunHilo)
hilo_2 = threading.Thread(target=algunHilo)

hilo_1.start()
hilo_2.start()

import os
import time
import multiprocessing

def kobeniFunction():
    os.system('python3 /home/daniel/proyectoquinto/senoresArduino.py')
    
def hanekawaFunction():
    os.system('python3 /home/daniel/proyectoquinto/Clases/onoff.py')

p1 = multiprocessing.Process(target=hanekawaFunction)
p2 = multiprocessing.Process(target=kobeniFunction)

if __name__ == "__main__":
    p1.start()
    p2.start()

    p1.join()
    p2.join()
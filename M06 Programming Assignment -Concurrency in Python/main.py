import multiprocessing
import time
import os
import random
from datetime import datetime

def mainProcess(main):
    print ("Process %s says: %s" % (os.getpid(), main))
    
if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=mainProcess, args=(("I'm function %s " % (n+1) + datetime.isoformat(datetime.now())) ,))
        p.start()
        time.sleep(random.random())
        p.terminate()
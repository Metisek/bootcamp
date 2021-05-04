import time

class TimeMeasure:
    
    def __init__(self):
        pass
    
    def __enter__(self):
        print("Rozpoczynam proces, czas jest mierzony")
        self.__start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Proces zakończono, czas nie jest już mierzony")
        self.__stop = time.time()
        print("Czas trwania:", self.__stop - self.__start)
        


with TimeMeasure() as mytimer:
    time.sleep(5)
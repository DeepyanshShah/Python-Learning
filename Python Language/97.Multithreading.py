import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    # ------------------------------------------------
    time1 = time.perf_counter()
    # Normal execution
    # func(4)
    # func(2)
    # func(1)
    # # calculating time
    # time2 = time.perf_counter()
    # print(time2-time1)
    # ---------------------------------------------------


    # Execution using threads
    t1 = threading.Thread(target=func, args=[4]) #initailizing thread
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start() #starting to execute thread
    t2.start()
    t3.start()

    t1.join() #awaits for thread to complete execution
    t2.join()
    t3.join()

    # calculating time
    time2 = time.perf_counter()
    print(time2-time1)

def poolingDemo():

    # with ThreadPoolExecutor() as executor:
    #     future1 = executor.submit(func,3)
    #     future2 = executor.submit(func,2)
    #     future3 = executor.submit(func,4)
    #     print(funture1.result())
    #     print(funture2.result())
    #     print(funture3.result())

        # OR

    with ThreadPoolExecutor() as executor:
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()
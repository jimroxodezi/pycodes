
import threading
import time


def task():
    for _ in range(10):
        time.sleep(0.1)



def bench_mark(n_threads):
    t1 = time.time()
    # tasks is a list containing thread objects
    tasks = [threading.Thread(target=task) for _ in range(n_threads)]

    # start the threads
    for thread in tasks:
        thread.start()

    # wait for the threads to finish
    for thread in tasks:
        thread.join()
    
    duration = time.time() - t1
    return duration


BENCHMARK_THREAD = [1,10,100,1_000,2_000,5_000,10_000]

if __name__ == '__main__':
    for n in BENCHMARK_THREAD:
        sec = bench_mark(n)
        print(f">>> threads ={n} took {sec} seconds")
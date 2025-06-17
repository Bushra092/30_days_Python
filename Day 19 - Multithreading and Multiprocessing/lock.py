

#! Lock

#? We have to use Lock when we are sharing memory.
#? Here, I am sharing a value, balance, which is accessed by both the deposit and withdraw functions.
#? If I don't use a Lock, both processes may try to read and write to balance.value at the same time, leading to inconsistent or unpredictable final values due to race conditions.
#? To prevent this, we use a Lock to ensure that only one process at a time can access and modify the shared memory

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        # balance.value = balance.value + 1
        # lock.release()
        with lock:
            balance.value += 1




def withdrow(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target = deposit , args = (balance,lock))
    w = multiprocessing.Process(target = withdrow , args = (balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)

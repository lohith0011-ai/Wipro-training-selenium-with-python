# IO bound tasks
'''

An I/O-bound task is a task where:

The program waits for data from external resources

CPU is mostly idle while waiting

Performance is limited by disk, network, or database speed

Examples of external resources:

Files

Network requests

Databases

APIs

User input

'''

# IO bound tasks

import time

def square_numbers():
    for i in range(10_000_000):
        i * i

start = time.time()

square_numbers()
square_numbers()

print("Time", time.time() - start)

# using multiprocessing concept

from multiprocessing import Process
import time

def square_numbers():
    for i in range(10_000_000):
        i * i

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=square_numbers)
    p2 = Process(target=square_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Time", time.time() - start)

#using pool (recommended Method)
from multiprocessing import Pool
import time
def square(n):
    return n*n
if __name__ == "__main__":
    numbers=[1,2,3,4,5]
    with Pool(processes=3) as pool:
        results=pool.map(square,numbers)
    print(results)


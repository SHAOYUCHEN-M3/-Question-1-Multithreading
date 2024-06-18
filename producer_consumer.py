import threading
import queue
import random
import time

# Shared queue
q = queue.Queue(maxsize=10)

# Thread-safe lock
lock = threading.Lock()

# Producer function
def producer():
    while True:
        if q.qsize() < 10:
            num = random.randint(1, 100)
            with lock:
                q.put(num)
                print(f"Produced {num}")
        time.sleep(0.1)

# Consumer function
def consumer():
    while True:
        if not q.empty():
            with lock:
                num = q.get()
                print(f"Consumed {num}")
        time.sleep(0.15)

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Let the program run for 10 seconds
time.sleep(10)

# Terminate the threads
producer_thread.join(timeout=1)
consumer_thread.join(timeout=1)

print("Program terminated.")
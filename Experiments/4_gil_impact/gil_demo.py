import threading
import time
import os

NUM_THREADS = 4
DURATION = 5  # seconds


def cpu_bound_task():
    end_time = time.time() + DURATION
    x = 0
    while time.time() < end_time:
        x += 1  # simple Python bytecode operation


if __name__ == "__main__":
    print(f"PID: {os.getpid()}")
    print(f"Starting {NUM_THREADS} CPU-bound threads for {DURATION} seconds")

    threads = []
    start = time.perf_counter()

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=cpu_bound_task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    print(f"Total execution time: {elapsed:.2f} seconds")

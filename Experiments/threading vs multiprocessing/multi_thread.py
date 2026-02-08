import time
import threading
from cpu_task import count_primes

START = 10_000
END = 500_000
NUM_THREADS = 4

results = []


def worker(start, end):
    results.append(count_primes(start, end))


if __name__ == "__main__":
    threads = []
    chunk_size = (END - START) // NUM_THREADS

    start_time = time.perf_counter()

    for i in range(NUM_THREADS):
        s = START + i * chunk_size
        e = START + (i + 1) * chunk_size
        t = threading.Thread(target=worker, args=(s, e))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start_time

    print(f"Primes found: {sum(results)}")
    print(f"Time taken (threads): {elapsed:.2f} seconds")

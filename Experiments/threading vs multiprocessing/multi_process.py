import time
from multiprocessing import Process, Queue
from cpu_task import count_primes

START = 10_000
END = 500_000
NUM_PROCESSES = 4


def worker(start, end, queue):
    queue.put(count_primes(start, end))


if __name__ == "__main__":
    processes = []
    queue = Queue()
    chunk_size = (END - START) // NUM_PROCESSES

    start_time = time.perf_counter()

    for i in range(NUM_PROCESSES):
        s = START + i * chunk_size
        e = START + (i + 1) * chunk_size
        p = Process(target=worker, args=(s, e, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total = sum(queue.get() for _ in processes)
    elapsed = time.perf_counter() - start_time

    print(f"Primes found: {total}")
    print(f"Time taken (processes): {elapsed:.2f} seconds")

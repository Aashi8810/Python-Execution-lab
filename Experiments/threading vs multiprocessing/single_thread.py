import time
from cpu_task import count_primes

START = 10_000
END = 500_000

if __name__ == "__main__":
    start_time = time.perf_counter()
    result = count_primes(START, END)
    elapsed = time.perf_counter() - start_time

    print(f"Primes found: {result}")
    print(f"Time taken (single thread): {elapsed:.2f} seconds")

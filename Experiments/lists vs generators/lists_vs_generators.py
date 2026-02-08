import time
from memory_profiler import memory_usage

N = 10_000_000


def list_version():
    data = [i * i for i in range(N)]
    return sum(data)


def generator_version():
    data = (i * i for i in range(N))
    return sum(data)


def measure(func):
    start_time = time.perf_counter()
    mem_usage = memory_usage(func, interval=0.01, max_iterations=1)
    elapsed = time.perf_counter() - start_time
    return max(mem_usage), elapsed


if __name__ == "__main__":
    print("Running list version...")
    list_mem, list_time = measure(list_version)

    print("Running generator version...")
    gen_mem, gen_time = measure(generator_version)

    print("\nResults:")
    print(f"List    → Peak memory: {list_mem:.2f} MiB, Time: {list_time:.2f} s")
    print(f"Generator → Peak memory: {gen_mem:.2f} MiB, Time: {gen_time:.2f} s")

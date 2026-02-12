import time


def optimized_function(n):
    total = 0
    for i in range(n):
        i_mod = i % 7
        for j in range(n):
            total += (i_mod * j) % 7
    return total


def main():
    start = time.perf_counter()
    result = optimized_function(3000)
    elapsed = time.perf_counter() - start
    print(f"Result: {result}")
    print(f"Time taken (optimized): {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()

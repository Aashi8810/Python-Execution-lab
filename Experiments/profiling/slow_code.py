from line_profiler import LineProfiler


def slow_function(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += (i * j) % 7
    return total


def main():
    lp = LineProfiler()
    lp.add_function(slow_function)

    lp.runctx("slow_function(3000)", globals(), locals())
    lp.print_stats()


if __name__ == "__main__":
    main()

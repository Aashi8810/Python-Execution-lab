import time

NUM_TASKS = 20
DELAY = 0.2


def fake_request(task_id):
    time.sleep(DELAY)
    return f"Result {task_id}"


if __name__ == "__main__":
    start = time.perf_counter()

    results = []
    for i in range(NUM_TASKS):
        results.append(fake_request(i))

    elapsed = time.perf_counter() - start
    print(f"Blocking I/O time: {elapsed:.2f} seconds")

import time
import threading

NUM_TASKS = 20
DELAY = 0.2

results = []


def fake_request(task_id):
    time.sleep(DELAY)
    results.append(f"Result {task_id}")


if __name__ == "__main__":
    start = time.perf_counter()

    threads = []
    for i in range(NUM_TASKS):
        t = threading.Thread(target=fake_request, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    print(f"Threaded I/O time: {elapsed:.2f} seconds")

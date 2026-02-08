import asyncio
import time

NUM_TASKS = 20
DELAY = 0.2


async def fake_request(task_id):
    await asyncio.sleep(DELAY)
    return f"Result {task_id}"


async def main():
    tasks = [fake_request(i) for i in range(NUM_TASKS)]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Async I/O time: {elapsed:.2f} seconds")

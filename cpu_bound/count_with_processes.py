from multiprocessing import Process
import time

MAX_COUNT = 100000000
NUM_PROCESSES = 4


def count(max_count: int) -> int:
    counter = 0
    for _ in range(max_count):
        counter += 1
    print("Finished")


if __name__ == "__main__":
    start_time = time.time()

    processes = [Process(target=count, args=(MAX_COUNT,)) for _ in range(NUM_PROCESSES)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f"Time elapsed: {time.time() - start_time}")

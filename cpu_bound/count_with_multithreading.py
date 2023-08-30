import threading
import time

MAX_COUNT = 100000000
NUM_PROCESSES = 4


def count(max_count):
    counter = 0
    for _ in range(max_count):
        counter += 1
    print("Finished")


if __name__ == "__main__":
    start_time = time.time()

    threads = [
        threading.Thread(target=count, args=(MAX_COUNT,)) for _ in range(NUM_PROCESSES)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Time elapsed: {time.time() - start_time}")

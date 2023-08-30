from multiprocessing import Pool
import time

MAX_COUNT = 100000000
NUM_PROCESSES = 4


def count(max_count: int) -> int:
    counter = 0
    for _ in range(max_count):
        counter += 1
    print("Finished")
    return counter


if __name__ == "__main__":
    start_time = time.time()

    results = Pool(NUM_PROCESSES).map(count, [MAX_COUNT] * 5)

    # imap is a generator, so it will return the results as they are ready
    # map converts all tasks to a list, and then passes them all at once to the workers, 
    # breaking them into chunks. imap on the other hand passes them one by one. 
    # This can be more memory efficient, but also slower.
    # results = Pool(NUM_PROCESSES).imap(count, [MAX_COUNT] * 5)
    # for result in results:
    #     print(result)
    
    print(f"Time elapsed: {time.time() - start_time}")
    print(results)

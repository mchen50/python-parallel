import threading
import time

NUM_CONSUMERS = 2

condition_satisfied = False

lock = threading.Lock()


def producer() -> None:
    global condition_satisfied

    while True:
        user_input = input("Enter a comamnd:")
        if user_input == "Start":
            # Signal the producers to start
            lock.acquire()
            condition_satisfied = True
            lock.release()
            break
        else:
            print(f"Unknown command {user_input}")
        time.sleep(1)


def consumer(consumer_idx: int) -> None:
    global condition_satisfied
    
    while True:
        lock.acquire()
        condition_satisfied_read = condition_satisfied
        lock.release()
        if condition_satisfied_read:
            for i in range(10):
                print(f"{i} from consumer {consumer_idx}")
                time.sleep(1)
            break
        time.sleep(1)


if __name__ == "__main__":
    threads = [threading.Thread(target=producer)] + [
        threading.Thread(target=consumer, args=(consumer_idx,))
        for consumer_idx in range(NUM_CONSUMERS)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

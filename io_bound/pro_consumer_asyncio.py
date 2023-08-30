import asyncio

NUM_CONSUMERS = 2

condition_satisfied = False
should_terminate = False


async def producer():
    global condition_satisfied

    while True:
        user_input = input("Enter a comamnd:")
        if user_input == "Start":
            # Signal the producers to start
            condition_satisfied = True
            break
        else:
            print(f"Unknown command {user_input}")
        await asyncio.sleep(1)


async def consumer(consumer_idx):
    global condition_satisfied

    while True:
        if condition_satisfied:
            for i in range(10):
                print(f"{i} from consumer {consumer_idx}")
                await asyncio.sleep(1)
            break
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(producer(), consumer(0), consumer(1))


if __name__ == "__main__":
    asyncio.run(main())

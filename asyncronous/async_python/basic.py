

import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(3)
    print("world")

# async def main():
    # await say_hello()


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    asyncio.run(say_hello())
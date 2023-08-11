

# import asyncio

# async def coro():
#     await asyncio.sleep(1)


# async def main():
#     print(type(coro()))
#     await coro()

# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
import time


async def say_after(delay: float, what: str):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, "hello")
    )

    task2 = asyncio.create_task(
        say_after(2, "world")
    )

    await task2
    await task1

# # TaskGroup() is in python3.11
# async def main():
#     async with asyncio.TaskGroup()

asyncio.run(main())
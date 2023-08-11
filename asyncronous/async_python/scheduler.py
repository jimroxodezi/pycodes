

import asyncio


async def greet(name: str):
    print(f"Hi, {name}. You're a coroutine")


if __name__ == "__main__":
    # asyncio.run(greet("Jimrox"))
    # deprecated
    loop = asyncio.get_event_loop()
    try:
        print("starting coroutine")
        coro = greet("Jimrox")
        print("entering event loop")
        loop.run_until_complete(coro)
    finally:
        print("closing event loop")
        loop.close()
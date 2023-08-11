

import asyncio, time

async def count():
    await asyncio.sleep(1)
    print("1")
    await asyncio.sleep(1)
    print("2")
    await asyncio.sleep(1)
    print("3")

async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    t1 = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t1
    print(f"Time elapsed: {t2:0.2f}")
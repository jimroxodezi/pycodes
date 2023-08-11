

import asyncio


async def outer():
    print("In outer")
    print("waiting for result 1")
    result1 = await phase1()
    print("waiting for result 2")
    result2 = await phase2(result1)
    return result1, result2



async def phase1():
    print("in phase 1")
    return "phase1 result"

async def phase2(arg):
    print("in phase 2")
    return "phase2 result derived from {}".format(arg)

if __name__ == "__main__":
    print(asyncio.run(outer()))
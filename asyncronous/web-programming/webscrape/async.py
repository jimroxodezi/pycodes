

import asyncio
import aiohttp
import time


async def download_file(url: str):
    print(f"Started downloading web page: {url}")
    async with aiohttp.ClientSession as session:
        async with session.get(url) as web_page:
            response = await web_page.read()
            print(f"Finished downloading web page: {url}")
            return response
        

async def write_file(n, content):
    filename = f"async_{n}.html"
    with open(filename, "wb") as f:
        print(f"Started writing {filename}")
        f.write(content)
        print(f'Finished writing {filename}')

async def scrape_task(n, url):
    content = await download_file(url)
    await write_file(n, content)

async def main():
    tasks = []
    for n, url in enumerate(open("urls.txt")):
        tasks.append(scrape_task(n, url))
    # asyncio.gather(*tasks)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    t = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter() - t
    print("Total time taken to scrape asyncronously: {t2}")
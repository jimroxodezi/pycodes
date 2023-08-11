
import asyncio
from aiohttp import ClientSession

URL = "http://localhost:3000/post-lang"

async def post_lang(url: str):
    async with ClientSession() as session:
        data = {"language": "python"}
        post_data = await session.post(url, data=data)
        print(await post_data.text())


asyncio.run(post_lang(URL))
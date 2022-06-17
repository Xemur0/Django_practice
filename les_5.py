import aiohttp
import asyncio


categories = [f"http://127.0.0.1:8000/goods/{i}/" for i in range(1, 10)]


async def get_category(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                with open(file_name, 'w', encoding='utf-8') as f:
                    print(data, file=f)
                print(f'{url} --- {file_name} --- OK')
            else:
                print(f"{url} --- {response.status} --- link doesn't exist")


result_file = [get_category(url, f'{i}.html')
               for i, url in enumerate(categories, start=1)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(result_file))

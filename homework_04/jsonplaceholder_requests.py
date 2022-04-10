"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)

- доработайте модуль `jsonplaceholder_requests`:
    - установите значения в константы `USERS_DATA_URL` и `POSTS_DATA_URL` (ресурсы нужно взять отсюда https://jsonplaceholder.typicode.com/)
    - создайте асинхронные функции для выполнения запросов к данным ресурсам (используйте `aiohttp`)
        - рекомендуется добавить базовые функции для запросов, которые будут переиспользованы (например `fetch_json`)

"""

import asyncio

from dataclasses import dataclass

from aiohttp import ClientSession, ClientResponse

from loguru import logger


FAKEAPI_URL = "https://jsonplaceholder.typicode.com"
USERS_DATA_URL = FAKEAPI_URL + "/users"
POSTS_DATA_URL = FAKEAPI_URL + "/posts"


# @dataclass
# class Service:
#     name: str
#     url: str
#     field: str


# SERVICES = [
#     Service("users", USERS_DATA_URL,"user"),
#     Service("posts", POSTS_DATA_URL,"post"),
# ]


async def fetch_json(session: ClientSession, url: str) -> dict:
    logger.info("Fetch url {}", url)
    async with session.get(url) as response: # type: ClientResponse
        response_json = await response.json()
        # logger.info("Fetched url {} and got data {}", response.url, response_json)
        return response_json

# async def fetch_data(service: Service) -> str:
#     async with ClientSession() as session:
#         data = await fetch_json(session, service.url)

#     logger.info("got data for service {}: {}", service.name, data)


# async def run_async_func():
#     coros = [
#         fetch_data(service)
#         for service in SERVICES
#     ]
#     logger.info("prepare {} coros")
#     tasks = [asyncio.create_task(coro) for coro in coros]
#     logger.info("start awaiting {} tasks")
#     await asyncio.wait(tasks)
#     logger.info("Finish running {} coros")

# async def main_async():

#     await run_async_func()

#     logger.info("Finishing main async")


# def main():
#     logger.info("Starting main")
#     asyncio.run(main_async())


# if __name__ == '__main__':
#     main()




# async def fetch_ip(service: Service) -> str:
#     async with ClientSession() as session:
#         data = await fetch_json(session, service.url)

#     logger.info("got data for service {}: {}", service.name, data)
#     return data.get(service.field, "")


# async def get_my_ip(timeout: float = 1) -> str:
#     my_ip = ""
#     tasks = {
#         asyncio.create_task(fetch_ip(service))
#         for service in SERVICES
#     }
#     logger.info("start processing tasks")

#     coro = asyncio.wait(
#         tasks,
#         timeout=timeout,
#         return_when=asyncio.ALL_COMPLETED,
#     )

#     done_tasks, pending_tasks = await coro
#     for pending_task in pending_tasks:
#         pending_task.cancel()
#         logger.info("Cancelled task {}", pending_task.get_name())

#     for task in done_tasks:
#         my_ip = task.result()
#         break
#     else:
#         logger.warning("could not fetch ip")

#     logger.info("done fetching ip: {}", my_ip)

#     return my_ip


# async def main():
#     logger.info("Start main")
#     my_ip = await get_my_ip(timeout=0.1)
#     return my_ip


# if __name__ == '__main__':
#     ip = asyncio.run(main())
#     logger.info("Result: {}", ip)
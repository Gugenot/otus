"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)

- доработайте модуль `jsonplaceholder_requests`:
    - установите значения в константы `USERS_DATA_URL` и `POSTS_DATA_URL` (ресурсы нужно взять отсюда https://jsonplaceholder.typicode.com/)
    - создайте асинхронные функции для выполнения запросов к данным ресурсам (используйте `aiohttp`)
        - рекомендуется добавить базовые функции для запросов, которые будут переиспользованы (например `fetch_json`)

"""


from aiohttp import ClientSession

from loguru import logger


FAKEAPI_URL = "https://jsonplaceholder.typicode.com"
USERS_DATA_URL = FAKEAPI_URL + "/users"
POSTS_DATA_URL = FAKEAPI_URL + "/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    logger.info("Fetch url {}", url)
    async with session.get(url) as response: 
        response_json = await response.json()
        return response_json

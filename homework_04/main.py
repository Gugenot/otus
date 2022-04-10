"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import config
from models import Base, User, Post
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL
from aiohttp import ClientSession, ClientResponse


engine = create_async_engine(
    config.SQLA_ASYNC_CONN_URI,
    echo=config.SQLA_ECHO,
)


async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_schemas():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(session: AsyncSession, url: str):

  async with ClientSession() as http_session:
    json_users_data = await fetch_json(http_session, url)
    for item in json_users_data:
        user = User(
          id=item["id"],
          name=item["name"],
          username=item["username"],
          email=item["email"]
        )
        session.add(user)


async def create_post(session: AsyncSession, url: str):

  async with ClientSession() as http_session:
    json_posts_data = await fetch_json(http_session, url)
    for item in json_posts_data:
        post = Post(
          id=item["id"],
          title=item["title"],
          body=item["body"],
          user_id=item["userId"]
        )
        session.add(post)


async def async_main():

    async with async_session() as session:
        await create_schemas()

        coro = asyncio.gather(
          create_user(session, USERS_DATA_URL), 
          create_post(session, POSTS_DATA_URL),
        )

        await coro
        await session.commit()


def main():

    asyncio.run(async_main())


if __name__ == "__main__":
    main()

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

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import config
from models import Base, User, Post
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL
from aiohttp import ClientSession

from loguru import logger


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

    logger.info("Enter module create_schemas")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def fetch_user_data():

  logger.info("Enter module fetch_user_data")
    
  async with ClientSession() as session:
    json_users_data = await fetch_json(session, USERS_DATA_URL)
    return json_users_data


async def fetch_post_data():

  logger.info("Enter module fetch_post_data")

  async with ClientSession() as session:
    json_posts_data = await fetch_json(session, POSTS_DATA_URL)
    return json_posts_data


async def save_data_to_db(session: AsyncSession, json_users_data: list, json_posts_data: list):

  logger.info("Enter module save_data_to_db")

  users = [
        User(
          id=item["id"],
          name=item["name"],
          username=item["username"],
          email=item["email"]
        ) 
        for item in json_users_data
  ]
  session.add_all(users)

  posts = [
        Post(
          id=item["id"],
          title=item["title"],
          body=item["body"],
          user_id=item["userId"]
        ) 
        for item in json_posts_data
  ]
  session.add_all(posts)

  await session.commit()


async def async_main():

  logger.info("Enter module async_main")

  async with async_session() as session:
    
    await create_schemas()

    json_users_data, json_posts_data = await asyncio.gather(
      fetch_user_data(), 
      fetch_post_data(),
    )

    await save_data_to_db(session, json_users_data, json_posts_data)


def main():

    logger.info("Enter module main")

    asyncio.run(async_main())


if __name__ == "__main__":
    main()

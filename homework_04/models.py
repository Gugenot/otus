"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

# import os

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

# Base = None
# Session = None


from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, declared_attr, relationship

import config

class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(config.SQLA_CONN_URI, echo=config.SQLA_ECHO)
Base = declarative_base(bind=engine, cls=Base)


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    name = Column(String(256), default=False, unique=True, nullable=False)
    username = Column(String(256), default=False, unique=True, nullable=False)
    email = Column(String(256), default=False, unique=True, nullable=False)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(" 
            f"id={self.id}, " 
            f"name={self.name!r}, " 
            f"username={self.username}, " 
            f"email={self.email!r})"
        )


class Post(Base):
    title = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=False,
        index=True,
    )

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id}, " \
               f"title={self.title!r}, " \
               f"body={self.body}, " \
               f"user_id={self.user_id!r})"

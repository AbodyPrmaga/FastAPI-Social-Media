from .init import engine, Base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import relationship

group_user = Table(
    "group_user",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id",ondelete="CASCADE"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id",ondelete="CASCADE"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    profile = relationship(
        "Profile", backref="user", uselist=False, cascade="all,delete,save-update"
    )
    posts = relationship(
        "Post", back_populates="user", cascade="all,delete,save-update"
    )
    groups = relationship("Group", secondary=group_user, back_populates="users",passive_deletes=True)

    def __repr__(self) -> str:
        return f"User : {self.username}"


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    bio = Column(String(100))
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    def __repr__(self) -> str:
        return f"Welcome {self.fname} {self.bio}"


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post = Column(Text(), nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    user = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"POST : {self.post}"


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50), nullable=False)
    users = relationship("User", secondary=group_user, back_populates="groups",passive_deletes=True)


Base.metadata.create_all(bind=engine)

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, desc, asc
from .models import User, Profile, Post, Group
from .init import engine

Session = sessionmaker(bind=engine)


def create_user(username: str, password: str, bio: str):
    session = Session()
    try:
        user = User(username=username, password=password)
        profile = Profile(name=username, bio=bio, user=user)
        session.add(user)
        session.add(profile)
        session.commit()
        session.refresh(user)
        session.refresh(profile)
    except:
        session.rollback()
        raise
    finally:
        session.close()


def read_users():
    session = Session()
    try:
        return session.query(User).all()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def update_user(user_id: int, username: str, bio: str):
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        user.username = username
        user.profile.bio = bio
        session.commit()
        session.refresh(user)
        return user
    except:
        session.rollback()
        raise
    finally:
        session.close()


def delete_user(user_id: int):
    session = Session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True
    except:
        session.rollback()
        raise
    finally:
        session.close()


def join_group(user_id: int, group_id: int):
    session = Session()
    try:
        if not user_id or not group_id:
            return False
        user = session.query(User).filter(User.id == user_id).first()
        group = session.query(Group).filter(Group.id == group_id).first()
        user.groups.append(group)
        session.commit()
        return True
    except:
        session.rollback()
        raise
    finally:
        session.close()


###################################


def fcreate_post(user_id: int, content: str):
    session = Session()
    try:
        if not user_id:
            return False
        post = Post(user_id=user_id, post=content)
        session.add(post)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_your_posts(user_id: int):
    session = Session()
    try:
        if not user_id:
            return False
        user = session.query(User).filter(User.id == user_id).first()
        return user.posts
    except:
        session.rollback()
        raise
    finally:
        session.close()


def edit_your_post(user_id: int, post_index: int, new_content: str):
    session = Session()
    try:
        if not user_id:
            return False
        user = session.query(User).filter(User.id == user_id).first()
        post_to_edit = user.posts[post_index]
        post_to_edit.post = new_content
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def del_post(user_id: int, post_index: int):
    session = Session()
    try:
        if user_id is None or post_index is None:
            return False
        user = session.query(User).filter(User.id == user_id).first()
        post = user.posts[post_index]
        session.delete(post)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


###################################
def get_groups():
    session = Session()
    try:
        return session.query(Group).all()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def create_ngroup(gname: str):
    session = Session()
    try:
        group = Group(group_name=gname)
        session.add(group)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def edit_group(group_id: int, new_name: str):
    session = Session()
    try:
        if group_id is None:
            return False
        group = session.query(Group).filter(Group.id == group_id).first()
        group.group_name = new_name
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def del_group(group_id: int):
    session = Session()
    try:
        group = session.query(Group).filter(Group.id == group_id).first()
        if not group:
            return False
        group.users = []
        session.delete(group)
        session.commit()
        return True

    except:
        session.rollback()
        raise
    finally:
        session.close()
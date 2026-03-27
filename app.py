from fastapi import FastAPI
from uvicorn import run
from model.utils import (create_user,
read_users,
update_user, 
delete_user,
fcreate_post,
get_your_posts,
edit_your_post,
create_ngroup,
join_group,
del_post,
get_groups,
del_group,
edit_group,)

app = FastAPI()

@app.get("/", tags=["User"])
async def get_users():
    return {"users": read_users()}

@app.post("/create_user", tags=["User"])
async def create_user_point(username: str, password: str, bio: str):
    create_user(username=username, password=password, bio=bio)
    return "Done Add New User Succssfully!"

@app.post("/join_group", tags=["User"])
async def join_the_group(user_id:int,group_id:int):
    join_group(user_id=user_id,group_id=group_id)
    return "Done Join The Group Succssfully!"

@app.put("/update_username", tags=["User"])
async def update_username(user_id: int, username: str, bio: str):
    update_user(user_id=user_id, username=username, bio=bio)
    return f"Done Update user by name : {username} , id : {user_id}"


@app.delete("/delete_user", tags=["User"])
async def delete_user_byid(user_id: int):
    delete_user(user_id=user_id)
    return "Done Delete User Succssfully!"

###################################

@app.get("/get_posts",tags=["Post"])
async def get_posts(user_id:int):
    return get_your_posts(user_id=user_id)
    
@app.post("/create_post", tags=["Post"])
async def create_post(user_id: int, content: str):
    fcreate_post(user_id=user_id, content=content)
    return "Done Add New Post Succssfully!"


@app.put("/update_post" , tags=["Post"])
async def update_post(user_id:int,post_index:int,new_content:str):
    edit_your_post(user_id=user_id,post_index=post_index,new_content=new_content)
    return "Done Edit Post Sucsssfully!"

@app.delete("/delete_post" ,tags=["Post"])
async def delete_the_post(user_id:int,post_index:int):
    del_post(user_id=user_id,post_index=post_index)
    return "Done Delete Post Sucsssfully!"

###################################
@app.get("/get_groups",tags=["Group"])
async def get_groups_point():
    return get_groups()

@app.post("/create_group", tags=["Group"])
async def create_new_group(gname:str):
    create_ngroup(gname=gname)
    return f"Done Create '{gname}' Group in APP Succssfully!"

@app.put("/update_group",tags=["Group"])
async def update_group(group_id:int,new_name:str):
    edit_group(group_id=group_id,new_name=new_name)
    return "Done Edit Group Sucsssfully!"

@app.delete("/delete_group",tags=["Group"])
async def del_group(group_id:int):
    del_group(group_id=group_id)
    return "Done Delete Group Sucsssfully!"

if __name__ == "__main__":
    run("app:app", reload=True)
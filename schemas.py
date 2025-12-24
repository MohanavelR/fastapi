from pydantic import BaseModel
class TodoBase(BaseModel):
    title:str
    desc:str | None =None
    is_completed:bool=False

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id:int
    class Congig:
        orm_mode=True
        
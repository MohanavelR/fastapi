from fastapi import FastAPI,Depends,HTTPException
from schemas import TodoCreate,TodoResponse
from sqlalchemy.orm import Session 
from db import get_db,Base,engine
from models import Todo
from typing import List
app=FastAPI()
Base.metadata.create_all(bind=engine)
# Post 
@app.post("/todos",response_model=TodoResponse)

def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    db_todo=Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
@app.get("/todos",response_model=List[TodoResponse])
def get_all_todos(db:Session=Depends(get_db)):
    return db.query(Todo).all()
@app.get("/todos/{id}",response_model=TodoResponse)
def get_todo(id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==id).first()
    if not todo:
      raise HTTPException(status_code=404,detail="Todo Not Found")
    return todo  

@app.put("/todos/{id}",response_model=TodoResponse)
def update_todo(id:int,update_todo:TodoCreate,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==id).first()
    if not todo:
      raise HTTPException(status_code=404,detail="Todo Not Found")
    for key,value in update_todo.dict().items():
       setattr(todo,key,value)
    db.commit()
    db.refresh(todo)
    return todo
@app.delete("/todos/{id}")
def delete_todo(id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==id).first()
    if not todo:
      raise HTTPException(status_code=404,detail="Todo Not Found")
    db.delete(todo)
    db.commit()
    return {"message":"Deleted Successfully"}    
 

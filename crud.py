import models

def get_all_todos(db):
    return db.query(models.Todo).all()

def get_todo(db, todo_id):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db, todo):
    new_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update_todo(db, todo_id, updated_data):
    todo = get_todo(db, todo_id)
    if todo:
        todo.title = updated_data.title
        todo.description = updated_data.description
        db.commit()
        db.refresh(todo)
    return todo

def delete_todo(db, todo_id):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
    return todo
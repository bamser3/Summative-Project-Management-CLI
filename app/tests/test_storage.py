import os
import pytest
from app.models.user_class import User
from app.models.project_class import Project
from app.models.task_class import Task
from app.storage.storage_class import Storage


@pytest.fixture

def storage():
    test_file = "data/test_database.json"
    

    if os.path.exists(test_file):
        os.remove(test_file)
    
    return Storage(file_path=test_file)

def test_save_and_load_users(storage):
    users = [User("Alice", "alice@example.com", "admin")]
    storage.save_users(users)
    loaded_users = storage.load_users()
    
    assert len(loaded_users) == 1
    assert loaded_users[0].username == "Alice"
    assert loaded_users[0].email == "alice@example.com"
    assert loaded_users[0].role == "admin"

def test_save_and_load_projects(storage):
    projects = [Project("Website", "Art site", "2026-07-05")]
    storage.save_projects(projects)
    loaded_projects = storage.load_projects()
    
    assert len(loaded_projects) == 1
    assert loaded_projects[0].title == "Website"
    assert loaded_projects[0].description == "Art site"
    assert loaded_projects[0].due_date == "2026-07-05"
    assert hasattr(loaded_projects[0], "id")

def test_save_and_load_tasks(storage):
    tasks = [Task("Website", "Connect API")]
    storage.save_tasks(tasks)
    loaded_tasks = storage.load_tasks()
    
    assert len(loaded_tasks) == 1
    assert loaded_tasks[0].project == "Website"
    assert loaded_tasks[0].title == "Connect API"
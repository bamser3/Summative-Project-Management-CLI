import sys
import pytest
from app.cli import main
from app.storage.storage_class import Storage
from app.models.user_class import User

def test_cli_add_user(tmp_path, monkeypatch):
    test_file = tmp_path / "db.json"
    monkeypatch.setattr("app.cli.Storage", lambda: Storage(file_path=str(test_file)))

    monkeypatch.setattr(sys, "argv", ["prog", "add-user", "--username", "Bob", "--email", "bob@mail.com", "--role", "admin"])
    
    main()
    
    storage = Storage(str(test_file))
    users = storage.load_users()
    
    assert len(users) == 1
    assert users[0].username == "Bob"
    

def test_add_user_missing_arguments(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "add-user", "--username", "Bob"]
    )

    with pytest.raises(SystemExit):
        main()
        
def test_list_users_empty(tmp_path, monkeypatch, capsys):
    from app.storage.storage_class import Storage
    from app.cli import list_users

    test_file = tmp_path / "db.json"

    monkeypatch.setattr(
        "app.cli.Storage",
        lambda: Storage(file_path=str(test_file))
    )

    list_users()

    captured = capsys.readouterr()
    assert "No users found." in captured.out
    
def test_complete_existing_task(tmp_path, monkeypatch, capsys):
    from app.storage.storage_class import Storage
    from app.models.task_class import Task
    from app.cli import complete_task

    test_file = tmp_path / "db.json"
    storage = Storage(file_path=str(test_file))

    task = Task("Website", "Connect API")
    storage.save_tasks([task])

    monkeypatch.setattr(
        "app.cli.Storage",
        lambda: Storage(file_path=str(test_file))
    )

    complete_task("Connect API")

    updated_tasks = storage.load_tasks()
    assert updated_tasks[0].completed is True

    captured = capsys.readouterr()
    assert "marked as complete" in captured.out
    
import sys
import pytest
from app.cli import main
from app.storage.storage_class import Storage


def test_full_user_project_task_workflow(tmp_path, monkeypatch):
    test_file = tmp_path / "db.json"

    # Redirect CLI Storage to temp file
    monkeypatch.setattr(
        "app.cli.Storage",
        lambda: Storage(file_path=str(test_file))
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "add-user",
         "--username", "Alice",
         "--email", "alice@mail.com",
         "--role", "admin"]
    )
    main()

    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "add-project",
         "--title", "Website",
         "--description", "Art site",
         "--due_date", "2026-12-01"]
    )
    main()

    tasks = ["Setup DB", "Build API", "Deploy"]

    for task in tasks:
        monkeypatch.setattr(
            sys,
            "argv",
            ["prog", "add-task",
             "--project", "Website",
             "--title", task]
        )
        main()

    for task in tasks[:2]:
        monkeypatch.setattr(
            sys,
            "argv",
            ["prog", "complete-task",
             "--title", task]
        )
        main()

    storage = Storage(file_path=str(test_file))
    saved_tasks = storage.load_tasks()

    assert len(saved_tasks) == 3

    completed_count = sum(task.completed for task in saved_tasks)
    assert completed_count == 2

    incomplete_count = sum(not task.completed for task in saved_tasks)
    assert incomplete_count == 1
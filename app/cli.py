import argparse
from app.models.user_class import User
from app.models.project_class import Project
from app.models.task_class import Task
from app.storage.storage_class import Storage

def main():
    parser = argparse.ArgumentParser(
    description="Project Management CLI tool",
    epilog="""
    Examples:
    python3 -m app add-user --username Alex --role admin
    python3 -m app add-project --title Website --description Art sharing website --due_date 01/12/1996 (1st of december 1996)
    python3 -m app add-task --project Website --title Connect-API
    """,
    formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")
    
    add_user_parser = subparsers.add_parser("add-user", help="Add a new user to the system")
    add_user_parser.add_argument("--username", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.add_argument("--role", required=True)
    
    add_project_parser = subparsers.add_parser("add-project", help="Create a new project")
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due_date", required=True)
    
    add_task_parser = subparsers.add_parser("add-task", help="Create a new task for a project")
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)
    
    subparsers.add_parser("list-users", help="List all users")
    subparsers.add_parser("list-projects", help="List all projects")
    subparsers.add_parser("list-tasks", help="List all tasks")
    
    mark_task_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    mark_task_parser.add_argument("--title", required=True)

    args = parser.parse_args()
    
    if args.command == "add-user":
        add_user(args.username, args.email, args.role)
    elif args.command == "add-project":
        add_project(args.title, args.description, args.due_date)
    elif args.command == "add-task":
        add_task(args.project, args.title)
    elif args.command == "complete-task":
        complete_task(args.title)
    elif args.command == "list-users":
        list_users()
    elif args.command == "list-projects":
        list_projects()
    elif args.command == "list-tasks":
        list_tasks()
    else:
        parser.print_help()
    

def add_user(username, email, role):
    storage = Storage()
    users = storage.load_users()
    
    user = User(username, email, role)
    users.append(user)
    
    storage.save_users(users)

def add_project(title, description, due_date):
    storage = Storage()
    projects = storage.load_projects()
    
    project = Project(title, description, due_date)
    projects.append(project)
    
    storage.save_projects(projects)
    
def add_task(project, title):
     storage = Storage()
     tasks = storage.load_tasks()
     
     task = Task(project, title)
     tasks.append(task)
     
     storage.save_tasks(tasks)
     
def list_users():
    storage = Storage()
    users = storage.load_users()
    if not users:
        print("No users found.")
    for user in users:
        print(f"{user.username} ({user.email}) - Role: {user.role}")

def list_projects():
    storage = Storage()
    projects = storage.load_projects()
    if not projects:
        print("No projects found.")
    for project in projects:
        print(f"[{project.id}] {project.title} - Due: {project.due_date} - {project.description}")

def list_tasks():
    storage = Storage()
    tasks = storage.load_tasks()
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        status = "Completed" if task.completed else "Not Complete"
        print(f"{status} {task.title} (Project: {task.project})")

def complete_task(title):
    storage = Storage()
    tasks = storage.load_tasks()
    found = False
    for task in tasks:
        if task.title == title:
            task.completed = True
            found = True
            break
    if found:
        storage.save_tasks(tasks)
        print(f"Task '{title}' marked as complete!")
    else:
        print(f"No task found with title '{title}'.")
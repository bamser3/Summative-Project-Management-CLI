# Project Management CLI

A simple command-line project management tool built in Python. You can add users, projects, and tasks, list them, and mark tasks as complete. Data is saved in a JSON file so it persists between runs.  

---

## Features

- Add users with username, email, and role.
- Create projects with title, description, and due date.
- Add tasks to projects.
- List all users, projects, and tasks.
- Mark tasks as complete.
- Stores data in `data/database.json`.

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/bamser3/Summative-Project-Management-CLI.git
   cd SummativeLab

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the CLI using:

```bash
python3 -m app <command> [options]
```

### Commands

* **Add a user**

  ```bash
  python3 -m app add-user --username Alex --email alex@mail.com --role admin
  ```

* **Add a project**

  ```bash
  python3 -m app add-project --title Website --description "Art sharing site" --due_date 2026-07-05
  ```

* **Add a task**

  ```bash
  python3 -m app add-task --project Website --title "Connect API"
  ```

* **List all users**

  ```bash
  python3 -m app list-users
  ```

* **List all projects**

  ```bash
  python3 -m app list-projects
  ```

* **List all tasks**

  ```bash
  python3 -m app list-tasks
  ```

* **Mark a task complete**

  ```bash
  python3 -m app complete-task --title "Connect API"
  ```

---

## Testing

Run tests with:

```bash
pytest
```

Tests check that users, projects, and tasks are correctly saved and loaded from the JSON storage file.

---

```
```

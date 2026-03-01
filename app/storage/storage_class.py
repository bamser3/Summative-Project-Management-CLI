import json

from app.models.user_class import User
from app.models.project_class import Project
from app.models.task_class import Task

class Storage:
    
    def __init__(self, file_path="data/database.json"):
        self.file_path = file_path
        
    def _load_data(self):
        try:
            with open(self.file_path, "r") as file:
                content = file.read().strip()
                if not content:
                    return {"users": [], "projects": [], "tasks": []}
                return json.loads(content)
        except FileNotFoundError:
            return {"users": [], "projects": [], "tasks": []}
        
    def _save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
            
        
    def save_users(self, users):
        data = self._load_data()
        data["users"] = [user.to_dict() for user in users]
        print(data) # im checking to make sure that the format of the data is correct
        self._save_data(data)
        
    def load_users(self):
        data = self._load_data()
        return [User(**user_dict) for user_dict in data["users"]]
        
    def save_projects(self, projects):
        data = self._load_data()
        data["projects"] = [project.to_dict() for project in projects]
        self._save_data(data)
        
    def load_projects(self):
        data = self._load_data()
        return [Project(**project_dict) for project_dict in data["projects"]]
    
    def save_tasks(self, tasks):
        data = self._load_data()
        data["tasks"] = [task.to_dict() for task in tasks]
        self._save_data(data)
        
    def load_tasks(self):
        data = self._load_data()
        return [Task(**task_dict) for task_dict in data["tasks"]]
            
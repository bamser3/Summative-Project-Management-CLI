class Task:
    def __init__(self, project, title, completed=False):
        self.project = project
        self.title = title  # setter validates
        self.completed = completed

    def __repr__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task(title='{self.title}', project='{self.project}', completed={status})"
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Title cannot be empty")
        self._title = value

    def to_dict(self):
        return {
            "title": self.title,
            "project": self.project,
            "completed": self.completed
        }
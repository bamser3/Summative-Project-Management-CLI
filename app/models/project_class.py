class Project:
    
    _id_counter = 1
    
    def __init__(self, title: str, description: str, due_date, id=None):
        if id is None:
            self.id = Project._id_counter
            Project._id_counter += 1
        else:
            self.id = id
            if id >= Project._id_counter:
                Project._id_counter = id + 1
        self.title = title
        self.description = description
        self.due_date = due_date
    
    def __repr__(self):
        return f"Project(title='{self.title}', due_date='{self.due_date}')"
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Title cannot be empty")
        self.__title = value
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "id": self.id
        }
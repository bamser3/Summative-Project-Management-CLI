class User: 
    def __init__(self, username: str, email: str, role: str):
        self.username = username
        self.role = role
        self.email = email
        self.projects = [] 
    
    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}', role='{self.role}')"
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Username cannot be empty")
        self._username = value
        
    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "role": self.role
        }
    
class User:
    def __init__(self, id, firstname, lastname, username, password, status, role_id):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.status = status
        self.role_id = role_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Invalid value for username it should be a string and more than 3 characters")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 6:
            raise ValueError("Invalid value for password it should be more than 6 characters")
        self._password = value

    def update(self,new_firstname, new_lastname, new_username, new_password, new_status, new_role):
        self.first_name = new_firstname
        self.last_name = new_lastname
        self.username = new_username
        self.password = new_password
        self.status = new_status
        self.role_id = new_role

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_role(self):
        if self.role_id == 1:
            return "Admin"
        elif self.role_id == 2:
            return "Default User"

    def get_status(self):
        if self.status == 1:
            return "Active"
        elif self.status == 2:
            return "Pending"
        elif self.status == 0:
            return "inactive"
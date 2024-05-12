class Privileges:
    def __init__(self, privileges: list[str]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Privileges: {self.privileges}")

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, email: str, cf: str, privileges: list[str]):
        super().__init__(first_name, last_name, age, email, cf)
        self.privileges = Privileges(privileges)

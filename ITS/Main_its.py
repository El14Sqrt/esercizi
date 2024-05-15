from ITS.Building import Building
from ITS.Group import Group
from ITS.People.Student import Student
from ITS.Room import Room


class Course:
    
    def __init__(self, name: str):
        self.name: str = name
        self.groups: list[Group] = []
        
    def register(self, student: Student):
        for group in self.get_groups():
            if group.add_student(student):
                break
        
    def get_groups(self) -> list[Group]:
        return self.groups
        
    def add_group(self, group: Group):
        if group and isinstance(group, Group)\
            and group not in self.groups:
            self.groups.append(group)
        
    
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=[-2,3])
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=[0,4])

smi.add_room(Room(id="666", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))
smi.add_room(Room(id="111", floor=-1, seats=32))

fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="cloud", limit=10)
cyber = Group(name="cyber", limit=10)

course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="1234", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="1234", name="Toni", surname="Mancini", age=46))
print(f'Studenti in fullstack: {len(course.groups[0].students)}')
print(f'Studenti in cloud: {len(course.groups[1].students)}')
print(f'Studenti in cyber: {len(course.groups[2].students)}')

class Person:
    _id_counter = 1

    def __init__(self, name, email):
        self.id = Person._id_counter
        Person._id_counter += 1
        self.name = name
        self.email = email


class User(Person):
    all = []

    def __init__(self, name, email):
        super().__init__(name, email)
        self._projects = []
        User.all.append(self)

    @property
    def projects(self):
        return self._projects
        #return [project for project in Project.all if project.user == self]

    def add_project(self, project):
        if not isinstance(project, Project):
            raise ValueError("project must be of type Project")
        self._projects.append(project)
        project.user = self

    @classmethod
    def get_all_users(cls):
        return cls.all
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"




class Project:
    all = []
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self._user = None
        self._tasks = []
        Project.all.append(self)

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("value must be an instance of User class")
        self._user = value

    @property
    def tasks(self):
        return self._tasks
        #return [task for task in Task.all if task.project==self]
    
    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("task must be a instance of Task class")
        self._tasks.append(task)
        task.assigned_to = self

    @classmethod
    def get_all_projects(cls):
        return cls.all
    
    def __repr__(self):
        return f"Project(user='{self._user}', title='{self.title}', description='{self.description}', due_date='{self.due_date}')"



class Task:
    all = []

    def __init__(self, title):
        self.title = title
        self.status = False
        self.assigned_to = None
        Task.all.append(self)

    def mark_complete(self):
        self.status = True

    @classmethod
    def get_all_tasks(cls):
        return cls.all
    
    def __repr__(self):
        if self.assigned_to:  ##self.assigned_to is a Project instance!
            project_title = self.assigned_to.title  ##self.assigned_to.title is the Project instance's property
        else:
            project_title = None
        return f"Task(project='{project_title}', title='{self.title}', status='{self.status}')"




# u1 = User("Alice", "alice@example.com")
# u2 = User("Bob", "bob@example.com")

# p1 = Project("Website", "Build landing page", "2025-06-10")
# p2 = Project("App", "Mobile app dev", "2025-07-01")

# u1.add_project(p1)
# u2.add_project(p2)

# t1 = Task("Design UI")
# t2 = Task("Write backend")

# p1.add_task(t1)
# p1.add_task(t2)

# print(User.get_all_users())      
# print(Project.get_all_projects())  
# print(Task.get_all_tasks())      

# """
# [User(id=1, name='Alice', email='alice@example.com'), User(id=2, name='Bob', email='bob@example.com')]

# [Project(user='User(id=1, name='Alice', email='alice@example.com')', title='Website', description='Build landing page', due_date='2025-06-10'), 
# Project(user='User(id=2, name='Bob', email='bob@example.com')', title='App', description='Mobile app dev', due_date='2025-07-01')]

# [Task(project='Website', title='Design UI', status='False'), Task(project='Website', title='Write backend', status='False')]
# """
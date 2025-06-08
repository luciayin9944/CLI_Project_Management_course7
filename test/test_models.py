import pytest
from lib.models import Person, User, Project, Task

def test_add_user():
    user = User("Alice", "alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.id == 1
    assert user in User.all

def test_add_project():
    project = Project("Build App", "An app project", "2025-12-01")
    assert project.title == "Build App"
    assert project.description == "An app project"
    assert project.due_date == "2025-12-01"
    assert project in Project.all


def test_add_task():
    task = Task("Design UI")
    assert task.title == "Design UI"
    assert not task.status
    task.mark_complete()
    assert task.status == True
    assert task in Task.all


def test_get_all():
    User.all.clear()
    Project.all.clear()
    Task.all.clear()

    u1 = User("Fay", "fay@example.com")
    u2 = User("Greg", "greg@example.com")
    assert User.get_all_users() == [u1, u2]

    p1 = Project("X", "x desc", "2025-01-01")
    p2 = Project("Y", "y desc", "2025-01-02")
    assert Project.get_all_projects() == [p1, p2]

    t1 = Task("Clean up")
    t2 = Task("Test all")
    assert Task.get_all_tasks() == [t1, t2]


def test_user_to_dict():
    User.all.clear()
    Person._id_counter = 1

    user = User("Dana", "dana@example.com")
    assert user.to_dict() == {
        "id": 1,
        "name": "Dana",
        "email": "dana@example.com"
    }


def test_project_to_dict():
    user = User("Eve", "eve@example.com")
    project = Project("Migration", "Move services", "2025-06-01")
    user.add_project(project)
    assert project.to_dict() == {
        "title": "Migration",
        "description": "Move services",
        "due_date": "2025-06-01",
        "user": "Eve"
    }


def test_task_to_dict():
    project = Project("Deployment", "Release system", "2025-11-11")
    task = Task("Push to prod")
    project.add_task(task)
    assert task.to_dict() == {
        "title": "Push to prod",
        "status": False,
        "project": "Deployment"
    }
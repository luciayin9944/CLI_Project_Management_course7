import argparse
from lib.models import User, Project, Task
from utils.helper import save_json, load_json
from utils.printer import success, error

users = {}
projects = {}
tasks = {}

def load_data():
    user_data = load_json("users.json")
    for u in user_data:
        user = User(u["name"], u["email"])
        users[user.name] = user

    project_data = load_json("projects.json")
    for p in project_data:
        user = users.get(p["user"])
        project = Project(p["title"], p["description"], p["due_date"])
        if user:
            user.add_project(project)
        projects[project.title] = project

    task_data = load_json("tasks.json")
    for t in task_data:
        project = projects.get(t["project"])
        task = Task(t["title"])
        if t["status"]:
            task.mark_complete()
        if project:
            project.add_task(task)
        tasks[task.title] = task


def save_data():
    save_json("users.json", [u.to_dict() for u in User.all])
    save_json("projects.json", [p.to_dict() for p in Project.all])
    save_json("tasks.json", [t.to_dict() for t in Task.all])



def add_new_user(args):
    if args.name in users:
        error(f"User '{args.name}' already exists.")
        #print(f"User '{args.name}' already exists.")

        return
    user = User(args.name, args.email)
    users[args.name] = user
    success(f"Added user: {user.name} with email {user.email}")
    #print(f"Added user: {user.name} with email {user.email}")
    save_data()


def list_users(args):
    for user in User.get_all_users():
        print(user)


def add_new_project(args):
    user = users.get(args.user_name)
    if not user:
        error(f"User '{args.user_name}' not found.")
        #print(f"User '{args.user_name}' not found.")
        return
    
    project = Project(args.title, args.description, args.due_date)
    user.add_project(project) ##calling User.add_project()
    projects[project.title] = project
    success(f"Created project '{project.title}' for user '{user.name}'")
    # print(f"Created project '{project.title}' for user '{user.name}'")
    save_data()

def list_projects(args):
    for project in Project.get_all_projects():
        print(project)


def add_new_task(args):
    project = projects.get(args.project_title)
    if not project:
        error(f"Project '{args.project_title}' not found.")
        #print(f"Project '{args.project_title}' not found.")
        return
    
    task = Task(args.title)
    project.add_task(task)
    tasks[task.title] = task
    success(f"Created task '{task.title}' and added to project '{project.title}'")
    #print(f"Created task '{task.title}' and added to project '{project.title}'")
    save_data()


def update_task_status(args):
    task = tasks.get(args.title)
    if not task:
        error(f"Task '{args.title}' not found.")
        #print(f"Task '{args.title}' not found.")
        return
    task.mark_complete()
    success(f"Marked task '{task.title}' as complete")
    #print(f"Marked task '{task.title}' as complete")
    save_data()

def list_tasks(args):
    for task in Task.get_all_tasks():
        print(task)



def main():
    load_data()

    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    # Add user
    user_parser = subparsers.add_parser("add-user", help="Add a new user")
    user_parser.add_argument("name", help="User name")
    user_parser.add_argument("email", help="User email")
    user_parser.set_defaults(func=add_new_user)

    # List users
    parser_list_users = subparsers.add_parser("list-users", help="List all users")
    parser_list_users.set_defaults(func=list_users)

    # Add project
    add_project_parser = subparsers.add_parser("add-project", help="Add a new project")
    add_project_parser.add_argument("user_name", help="User name to assign the project to")
    add_project_parser.add_argument("title", help="Project title")
    add_project_parser.add_argument("description", help="Project description")
    add_project_parser.add_argument("due_date", help="Project due date")
    add_project_parser.set_defaults(func=add_new_project)

    # List projects
    parser_list_projects = subparsers.add_parser("list-projects", help="List all projects")
    parser_list_projects.set_defaults(func=list_projects)


    # Add task
    add_task_parser = subparsers.add_parser("add-task", help="Add a task to a project")
    add_task_parser.add_argument("project_title", help="Title of the project")
    add_task_parser.add_argument("title", help="Task title")
    add_task_parser.set_defaults(func=add_new_task)

    # Complete task
    complete_task_parser = subparsers.add_parser("update-task-status", help="Mark a task as complete")
    complete_task_parser.add_argument("title", help="Task title")
    complete_task_parser.set_defaults(func=update_task_status)

    # List tasks
    parser_list_tasks = subparsers.add_parser("list-tasks", help="List all tasks")
    parser_list_tasks.set_defaults(func=list_tasks)


    # Parse arguments
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

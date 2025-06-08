import argparse
from lib.models import User, Project, Task

users = {}
projects = {}
tasks = {}

def add_user(args):
    if args.name in users:
        print(f"User '{args.name}' already exists.")
        return
    user = User(args.name, args.email)
    users[args.name] = user
    print(f"Added user: {user.name} with email {user.email}")


def add_project(args):
    user = users.get(args.user_name)
    if not user:
        print(f"User '{args.user_name}' not found.")
        return
    
    project = Project(args.title, args.description, args.due_date)
    projects[args.title] = project
    print(f"Created project '{project.title}' for user '{user.name}'")


def add_task(args):
    project = projects.get(args.project_title)
    if not project:
        print(f"Project '{args.project_title}' not found.")
        return
    
    task = Task(args.title)
    project.add_task(task)
    tasks[args.title] = task
    print(f"Created task '{task.title}' and added to project '{project.title}'")


def update_task_status(args):
    task = tasks.get(args.title)
    if not task:
        print(f"Task '{args.title}' not found.")
        return
    
    task.mark_complete()
    print(f"Marked task '{task.title}' as complete")


def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    # Add user
    user_parser = subparsers.add_parser("add-user", help="Add a new user")
    user_parser.add_argument("name", help="User name")
    user_parser.add_argument("email", help="User email")
    user_parser.set_defaults(func=add_user)

    # Add project
    add_project_parser = subparsers.add_parser("add-project", help="Add a new project")
    add_project_parser.add_argument("user_name", help="User name to assign the project to")
    add_project_parser.add_argument("title", help="Project title")
    add_project_parser.add_argument("description", help="Project description")
    add_project_parser.add_argument("due_date", help="Project due date")
    add_project_parser.set_defaults(func=add_project)

    # Add task
    add_task_parser = subparsers.add_parser("add-task", help="Add a task to a project")
    add_task_parser.add_argument("project_title", help="Title of the project")
    add_task_parser.add_argument("title", help="Task title")
    add_task_parser.set_defaults(func=add_task)

    # Complete task
    complete_task_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_task_parser.add_argument("title", help="Task title")
    complete_task_parser.set_defaults(func=update_task_status)


    # Parse arguments
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

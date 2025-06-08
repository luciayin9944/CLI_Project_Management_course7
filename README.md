# CLI Project Management Tool

A simple command-line project management tool for developer teams. This tool allows administrators to manage users, projects, and tasks through structured CLI commands.

## Features

•	Add and manage users
•	Assign projects to users
•	Create and update tasks under projects
•	Intuitive CLI commands for quick management

## Installation
    # Clone the repository
    git clone https://github.com/luciayin9944/CLI_Project_Management_course7.git
    cd CLI_Project_Management_course7

    # Set up virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Run the tool
    python main.py --help


## Usage
Example CLI commands:

    python main.py add-user Alice alice@example.com 
    python main.py add-project Alice "Website Redesign" "Change company site" "2025-07-01"
    python main.py add-task "Website Redesign" "Create wireframes"
    python main.py list-users
    python main.py list-projects
    python main.py list-tasks
    python main.py update-task-status "Create wireframes"
    python main.py list-tasks

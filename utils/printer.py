from rich.console import Console

console = Console()

def success(msg):
    console.print(f"[bold green]{msg}[/bold green]")

def error(msg):
    console.print(f"[bold red]{msg}[/bold red]")

def info(msg):
    console.print(f"[bold blue]{msg}[/bold blue]")
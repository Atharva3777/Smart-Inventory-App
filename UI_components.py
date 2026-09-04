import time

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box

console = Console()


# ----------------------------- Layout ------------------------------ #

def show_banner():
    console.print()
    console.print(Rule("[bold cyan]Smart Inventory App[/bold cyan]", style="cyan"))


def show_menu():
    console.print()
    console.print(
        Panel.fit(
            "[bold][gold1]1. Add Item[gold1][/bold]\n"
            "[bold]2. Update Item[/bold]\n"
            "[bold]3. Show Items[/bold]\n"
            "[bold]4. Delete Item[/bold]\n"
            "[bold]5. Export To Excel[/bold]\n"
            "[bold]6. Exit[/bold]",
            title="[hot_pink]Menu[/hot_pink]",
            border_style="bold cyan",
        )
    )


def section_rule(title=""):
    console.print(Rule(f"[bold][red1]{title}[/red1][/bold]", style="cyan"))


# ----------------------------- Table -------------------------------- #

def show_inventory_table(inventory_dict):
    if not inventory_dict:
        show_warning("Inventory is empty.")
        return

    table = Table(
        title="Smart Inventory App",
        title_justify="center",
        box=box.ROUNDED,
        header_style="bold cyan",
    )
    table.add_column("Product ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("[magenta]Product Name[/magenta]", style="magenta", justify="center")
    table.add_column("[yellow]Category[/yellow]", justify="center", style="yellow")
    table.add_column("[green]Price[/green]", justify="right", style="green")
    table.add_column("[green]Quantity[/green]", justify="right", style="green")
    table.add_column("[red]Supplier[/red]", justify="center", style="red")

    for product_id, item in inventory_dict.items():
        table.add_row(
            str(product_id),
            item.product_name,
            item.category,
            f"{item.price}",
            str(item.quantity),
            item.supplier,
        )

    console.print(table)


# ----------------------------- Messages ------------------------------ #

def show_success(message):
    console.print(f"[bold green]\u2714  {message}[/bold green]")


def show_error(message):
    console.print(f"[bold red]\u2716  {message}[/bold red]")


def show_warning(message):
    console.print(f"[bold yellow]\u26a0  {message}[/bold yellow]")


def show_info(message):
    console.print(f"[bold blue]\u2139  {message}[/bold blue]")


# ----------------------------- Prompts -------------------------------- #

def ask_text(prompt_text):
    return Prompt.ask(f"[bold cyan]{prompt_text}[/bold cyan]")


def ask_int(prompt_text):
    return IntPrompt.ask(f"[bold cyan]{prompt_text}[/bold cyan]")


def ask_confirm(prompt_text):
    return Confirm.ask(f"[bold cyan]{prompt_text}[/bold cyan]")


# ----------------------------- Progress -------------------------------- #

def run_progress(task_description, total_steps=50, step_delay=0.02):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(task_description, total=total_steps)
        for _ in range(total_steps):
            time.sleep(step_delay)
            progress.advance(task)
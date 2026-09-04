# Smart Inventory App

A lightweight, terminal-based inventory management tool for Python. Add, update, browse, and delete stock records through a clean interactive menu, then export your full inventory to Excel whenever you need it.

Built with [Rich](https://github.com/Textualize/rich) for a colorful, table-driven CLI — no database, no web server, no config files.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Getting Help](#getting-help)
- [Contributing & Maintainers](#contributing--maintainers)

## Features

- **Full CRUD workflow** — add, update, view, and delete inventory items from a simple numbered menu
- **Polished terminal UI** — Rich-powered tables, panels, colored status messages, and progress bars replace plain `print()` output
- **Guardrails built in** — duplicate product IDs are rejected on add, and deletes require an explicit yes/no confirmation
- **One-click Excel export** — dump the current inventory to a `.xlsx` file from the menu, with progress feedback while it writes
- **Zero setup** — in-memory data model, no database or config; clone it and run it

## Getting Started

### Prerequisites

- Python 3.10 or later (the codebase uses `match`/`case` pattern matching)
- pip

### Installation

Clone the repository and install the dependencies:

```bash
git clone <your-repo-url>
cd smart-inventory-app
pip install rich pandas openpyxl
```

| Package | Why it's needed |
|---|---|
| `rich` | Powers every table, panel, colored message, and progress bar in the CLI |
| `pandas` | Builds the data table used for Excel export |
| `openpyxl` | Excel engine `pandas` uses to write `.xlsx` files |

### Running the app

```bash
python main.py
```

## Usage

On launch you'll see a numbered menu:

```
───────────────────────── Smart Inventory  App ─────────────────────────

╭─────── Menu ───────╮
│ 1. Add Item        │
│ 2. Update Item     │
│ 3. Show Items      │
│ 4. Delete Item     │
│ 5. Export To Excel │
│ 6. Exit            │
╰────────────────────╯
Enter your choice (1-6):
```

Pick a number and follow the prompts:

- **Add Item (1)** — walks you through product ID, name, category, price, quantity, and supplier. Duplicate IDs are rejected.
- **Update Item (2)** — look up a product by ID, then choose which single field to change.
- **Show Items (3)** — renders the full inventory as a formatted table:

  ```
                               Smart Inventory 
  ╭────────────┬──────────────┬─────────────┬───────┬──────────┬───────────╮
  │ Product ID │ Product Name │  Category   │ Price │ Quantity │ Supplier  │
  ├────────────┼──────────────┼─────────────┼───────┼──────────┼───────────┤
  │    101     │   Keyboard   │ Electronics │  1500 │       10 │ Acme Corp │
  ╰────────────┴──────────────┴─────────────┴───────┴──────────┴───────────╯
  ```

- **Delete Item (4)** — look up a product by ID and confirm before it's removed.
- **Export To Excel (5)** — prompts for a filename, shows a progress bar, and writes a `.xlsx` file to the project root.
- **Exit (6)** — ends the session.

> **Note:** Inventory lives in memory for the current run only — it resets each time you restart the app. There is no persistence layer yet.

## Project Structure

```
.
├── main.py                   # Entry point; runs the interactive menu loop
├── inventory_management.py   # Core inventoryManager class (add/update/show/delete/export)
├── UI_components.py          # All Rich-based presentation (tables, panels, prompts, messages, progress bars)
└── excel.py                  # Standalone helper that exports inventory data to .xlsx via pandas
```

### Main components

- **`inventoryManager` (`inventory_management.py`)** — a classmethod-driven class that holds the in-memory `inventory_list` dict (keyed by product ID) and exposes `add_item()`, `update_item()`, `show_item()`, `delete_item()`, and `convert_excel()`. It calls out to `UI_components` for every prompt and message, keeping business logic free of display code.
- **`UI_components.py`** — a thin presentation layer built on Rich. Wraps `rich.table.Table`, `rich.panel.Panel`, and `rich.prompt` so the rest of the app never calls `print()`/`input()` directly. Exposes helpers like `show_inventory_table()`, `ask_int()`, `show_success()`, and `run_progress()`.
- **`excel.py`** — a single function, `export_to_excel(inventory_dict, filename)`, that converts the inventory dict into a `pandas.DataFrame` and writes it out. Kept dependency-free from `inventory_management.py` to avoid a circular import.
- **`main.py`** — the entry point. Runs the menu loop and dispatches each numbered choice to the matching `inventoryManager` method.

## Getting Help

- Have a question or found a bug? Open an [issue](../../issues) on this repository.
- Check existing [issues](../../issues) first — your question may already be answered there.

## Contributing & Maintainers

This project is maintained by the repository owner. Contributions are welcome:

1. Fork the repository and create a feature branch.
2. Make your changes, keeping presentation logic in `UI_components.py` and business logic in `inventory_management.py`.
3. Open a pull request describing what changed and why.

No `LICENSE` file is currently included in this repository — check with the maintainer before reusing the code elsewhere.

import UI_components as ui
from excel import export_to_excel


class inventoryManager:

    inventory_list = {}

    def __init__(self, product_id, product_name, category, price, quantity, supplier):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    @classmethod
    def add_item(cls):
        ui.section_rule("Add New Item")

        product_id = ui.ask_int("Enter product id")
        if product_id in cls.inventory_list:
            ui.show_error(f"A product with ID {product_id} already exists.")
            return

        product_name = ui.ask_text("Enter product name")
        category = ui.ask_text("Enter category")
        price = ui.ask_int("Enter the price")
        quantity = ui.ask_int("Enter number of items")
        supplier = ui.ask_text("Enter Supplier")

        item = cls(product_id, product_name, category, price, quantity, supplier)
        cls.inventory_list[product_id] = item

        ui.show_success("Item added successfully!")

    @classmethod
    def show_item(cls):
        ui.section_rule("Inventory")
        ui.show_inventory_table(cls.inventory_list)

    @classmethod
    def update_item(cls):
        ui.section_rule("Update Item")

        fetch_id = ui.ask_int("Enter the product id for updating record")
        if fetch_id not in cls.inventory_list:
            ui.show_error("Item not in inventory")
            return

        item = cls.inventory_list[fetch_id]

        ui.console.print(
            "[bold]1.[/bold] Product Name\n"
            "[bold]2.[/bold] Category\n"
            "[bold]3.[/bold] Price\n"
            "[bold]4.[/bold] Quantity\n"
            "[bold]5.[/bold] Supplier"
        )
        choice = ui.ask_int("Enter the choice")

        match choice:
            case 1:
                item.product_name = ui.ask_text("Enter new product name")
            case 2:
                item.category = ui.ask_text("Enter new category")
            case 3:
                item.price = ui.ask_int("Enter new price")
            case 4:
                item.quantity = ui.ask_int("Enter new quantity")
            case 5:
                item.supplier = ui.ask_text("Enter new supplier")
            case _:
                ui.show_error("Wrong input!")
                return

        ui.show_success("Item updated successfully!")

    @classmethod
    def delete_item(cls):
        ui.section_rule("Delete Item")

        fetch_id = ui.ask_int("Enter the product you want to delete")
        if fetch_id not in cls.inventory_list:
            ui.show_error("Item not in the inventory")
            return

        if ui.ask_confirm(f"Are you sure you want to delete product {fetch_id}?"):
            del cls.inventory_list[fetch_id]
            ui.show_success("Item deleted successfully")
        else:
            ui.show_info("Deletion cancelled")

    @classmethod
    def convert_excel(cls):
        ui.section_rule("Export To Excel")

        if not cls.inventory_list:
            ui.show_warning("Inventory is empty. Nothing to export.")
            return

        filename = ui.ask_text("Enter filename (without extension)").strip() or "inventory"
        filename = f"{filename}.xlsx"

        ui.run_progress("Exporting inventory to Excel...")

        try:
            export_to_excel(cls.inventory_list, filename)
            ui.show_success(f"Inventory exported to '{filename}' successfully!")
        except Exception as e:
            ui.show_error(f"Export failed: {e}")
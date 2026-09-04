from inventory_management import inventoryManager
import UI_components as ui


def menu():
    ui.show_banner()

    while True:
        ui.show_menu()
        choice = ui.ask_int("Enter your choice (1-6)")

        match choice:
            case 1:
                inventoryManager.add_item()
            case 2:
                inventoryManager.update_item()
            case 3:
                inventoryManager.show_item()
            case 4:
                inventoryManager.delete_item()
            case 5:
                inventoryManager.convert_excel()
            case 6:
                ui.show_success("Thank you for using the App!")
                break
            case _:
                ui.show_error("Wrong input")


if __name__ == "__main__":
    menu()
import pandas as pd


def export_to_excel(inventory_dict, filename="inventory.xlsx"):
    records = [
        {
            "Product ID": product_id,
            "Product Name": item.product_name,
            "Category": item.category,
            "Price": item.price,
            "Quantity": item.quantity,
            "Supplier": item.supplier,
        }
        for product_id, item in inventory_dict.items()
    ]

    df = pd.DataFrame(records)
    df.to_excel(filename, index=False)
    return filename
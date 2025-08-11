import json
import os

inventory = {}

# ---------- Load Inventory ----------
def load_inventory(filename="inventory.json"):
    global inventory
    if os.path.exists(filename):
        with open(filename, "r") as file:
            inventory = json.load(file)
            print("✅ Inventory loaded successfully.")
    else:
        print("⚠️ No existing inventory file found. Starting fresh.")

# ---------- Save Inventory ----------
def save_inventory(filename="inventory.json"):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)
    print("✅ Inventory saved successfully.")

# ---------- Add Item ----------
def add_item():
    try:
        name = input("Enter item name: ").strip()
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"qty": qty, "price": price}
        print(f"✅ Item '{name}' added successfully.")
    except ValueError:
        print("❌ Invalid input. Quantity must be an integer and price must be a number.")

# ---------- Update Item ----------
def update_item():
    name = input("Enter item name to update: ").strip()
    if name in inventory:
        try:
            qty = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[name] = {"qty": qty, "price": price}
            print(f"✅ Item '{name}' updated successfully.")
        except ValueError:
            print("❌ Invalid input. Quantity must be an integer and price must be a number.")
    else:
        print(f"❌ Item '{name}' not found.")

# ---------- View Inventory ----------
def view_inventory():
    if not inventory:
        print("📦 Inventory is empty.")
        return
    print("\n📋 Current Inventory:")
    print("{:<20} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    print("-" * 40)
    for name, details in inventory.items():
        print("{:<20} {:<10} ${:<10.2f}".format(name, details['qty'], details['price']))
    print()

# ---------- Search Item ----------
def search_item():
    name = input("Enter item name to search: ").strip()
    if name in inventory:
        item = inventory[name]
        print(f"🔍 Found '{name}': Quantity = {item['qty']}, Price = ${item['price']:.2f}")
    else:
        print(f"❌ Item '{name}' not found.")

# ---------- Menu ----------
def show_menu():
    print("\n====== Inventory Management System ======")
    print("1. Add Item")
    print("2. Update Item")
    print("3. View Inventory")
    print("4. Search Item")
    print("5. Save Inventory")
    print("6. Load Inventory")
    print("7. Exit")

# ---------- Main Loop ----------
def main():
    load_inventory()
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            search_item()
        elif choice == '5':
            save_inventory()
        elif choice == '6':
            load_inventory()
        elif choice == '7':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 7.")

if __name__ == "__main__":
    main()

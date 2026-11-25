
import csv
import sys

def display_items(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            print("\nGrocery Inventory")
            print("-" * 50)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("Error: File not found.")

def search_item(filename, item_id):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["ItemID"] == item_id:
                    print("\nItem Found:")
                    print(row)
                    return

            print("Item not found.")

    except FileNotFoundError:
        print("Error: File not found.")

if len(sys.argv) < 2:
    print("Usage: python grocery.py <filename>")
else:
    filename = sys.argv[1]

    display_items(filename)

    item_id = input("\nEnter Item ID to search: ")
    search_item(filename, item_id)

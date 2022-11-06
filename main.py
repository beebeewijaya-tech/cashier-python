from controllers.transaction import create_transaction, delete_transaction, get_transaction
from controllers.item import add_new_item, check_order, delete_all_item, delete_item, print_table, total_price, update_item_name, update_item_price, update_item_qty
from db.table import create_table

create_table()

IS_PLAY = True

# TRX only can be once per session
# Need to clear TRX every exit
TRX = None

while IS_PLAY:
    print("""........... Choose the task ........... 
        1. Add New Transaction
        2. Use existing transaction
        3. Add New Item Into Transaction
        4. Update Item Price
        5. Update Item Name
        6. Update Item Qty
        7. Delete Item
        8. Reset Transaction
        9. Delete Transaction
        10. Check Order
        11. Total Price
        12. Exit
    """)

    print("--------------------------------")
    print("\n")

    resp = input("Enter task no: ")

    match resp:
        case "1":
            if TRX is not None:
                print("You have active transaction!")
                print("Delete the transaction first!")
                continue
            TRX = create_transaction()
            print("Transaction Created...")

        case "2":
            if TRX is not None:
                print("You have active transaction!")
                print("Delete the transaction first!")
                continue
            TRX = get_transaction()
            if TRX is None:
                print("Create the transaction first!")
                continue
            print("Use existing transaction...")

        case "3":
            if TRX is None:
                print("Create the transaction first!")
                continue
            TRX = add_new_item(TRX)
            print("Item added!")

        case "4":
            if TRX is None:
                print("Create the transaction first!")
                continue
            TRX = update_item_price(TRX)
            if TRX is None:
                print("Unable to update item price! Item not found!")
                continue
            print("Item price updated!")

        case "5":
            if TRX is None:
                print("Create the transaction first!")
                continue
            TRX = update_item_name(TRX)
            if TRX is None:
                print("Unable to update item name! Item not found!")
                continue
            print("Item name updated!")

        case "6":
            if TRX is None:
                print("Create the transaction first!")
                continue
            TRX = update_item_qty(TRX)
            if TRX is None:
                print("Unable to update item qty! Item not found!")
                continue
            print("Item qty updated!")

        case "7":
            if TRX is None:
                print("Create the transaction first!")
                continue
            TRX = delete_item(TRX)
            if TRX is None:
                print("Unable to delete item! Item not found!")
                continue
            print("Item deleted!")

        case "8":
            if TRX is None:
                print("Create the transaction first!")
                continue
            TRX = delete_all_item(TRX)
            print("All item on transaction deleted!")

        case "9":
            if TRX is None:
                print("Create the transaction first!")
                continue
            delete_transaction(TRX)
            TRX = None
            print("Transaction Deleted!")

        case "10":
            if TRX is None:
                print("Create the transaction first!")
                continue
            item = check_order(TRX)
            if item is None:
                print("Item is empty! please add item to the transaction")
                continue
            print(print_table(item))
            print("\n")

        case "11":
            if TRX is None:
                print("Create the transaction first!")
                continue
            item = check_order(TRX)
            if item is None:
                print("Item is empty! please add item to the transaction")
                continue
            total = total_price(item)
            print(total)
            print("\n")

        case "12" | "":
            print("Exit cashier apps")
            print("-----------------")
            TRX = None
            IS_PLAY = False

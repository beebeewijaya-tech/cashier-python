from uuid_extensions import uuid7
from tabulate import tabulate
from models.transaction import Transaction
from helpers.order import check_order_utils
from models.item import Item


def add_new_item(trx: Transaction):
    item_name = input("Enter item name: ")
    item_price = input("Enter item price: ")
    item_qty = input("Enter item qty: ")

    item = Item(
        id=str(uuid7()),
        name=item_name,
        price=item_price,
        qty=item_qty
    )

    trx.add_item(item=item)
    data = {}
    data[item_name] = [item_qty, item_price]
    return trx, data


def update_item_price(trx: Transaction):
    item_name = input("Enter item name: ")
    item_price = input("Enter item price: ")

    item = trx.get_item(item_name)
    if item is None:
        return None

    trx.update_item_price(name=item_name, price=item_price)
    return trx


def update_item_name(trx: Transaction):
    item_name = input("Enter item name: ")
    item_new_name = input("Enter item new name: ")

    item = trx.get_item(item_name)
    if item is None:
        return None

    trx.update_item_name(name=item_name, new_name=item_new_name)
    return trx


def update_item_qty(trx: Transaction):
    item_name = input("Enter item name: ")
    item_qty = input("Enter item qty: ")

    item = trx.get_item(item_name)
    if item is None:
        return None

    trx.update_item_qty(name=item_name, qty=item_qty)
    return trx


def delete_item(trx: Transaction):
    item_name = input("Enter item name: ")

    item = trx.get_item(item_name)
    if item is None:
        return None

    result = trx.get_item(item_name)
    trx.delete_item(name=item_name)

    data = {}
    data[item_name] = [result[2], result[3]]
    return trx, data


def delete_all_item(trx: Transaction):
    trx.delete_all_item()
    return trx


def check_order(trx: Transaction):
    item = trx.all_item()
    if item is None:
        return None

    is_invalid = False
    item_arr = []
    for i in item:
        arr = list(i)
        invalid = check_order_utils(i)
        if invalid:
            is_invalid = True
        else:
            arr.append(i[1] * i[2])

        item_arr.append(arr)

    print("\n")
    if is_invalid:
        print("Terjadi kesalahan pada input data!")
    else:
        print("Pemesanan sudah benar")

    return item_arr


def print_table(item):
    table_item = tabulate(
        item, headers=["Name", "Qty", "Price", "Transaction ID", "Total Price"])

    return table_item


def total_price(item):
    total = 0
    discount = 0

    for i in item:
        total += i[-1]

    if total > 200000:
        discount = 5
    elif total > 300000:
        discount = 8
    elif total > 500000:
        discount = 10
    else:
        discount = 0

    return f"Total belanja anda sebesar {total}, anda mendapatkan diskon sebesar {discount}%"
